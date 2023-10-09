# Copyright (c) 2006-2008 The Trustees of Indiana University.                   
# All rights reserved.                                                          
#                                                                               
# Redistribution and use in source and binary forms, with or without            
# modification, are permitted provided that the following conditions are met:   
#                                                                               
# - Redistributions of source code must retain the above copyright notice, this 
#   list of conditions and the following disclaimer.                            
#                                                                               
# - Redistributions in binary form must reproduce the above copyright notice,   
#   this list of conditions and the following disclaimer in the documentation   
#   and/or other materials provided with the distribution.                      
#                                                                               
# - Neither the Indiana University nor the names of its contributors may be used
#   to endorse or promote products derived from this software without specific  
#   prior written permission.                                                   
#                                                                               
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"   
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE     
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE   
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL    
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER    
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.          

__doc__="""
An implementation of InstructionStream that conforms to the OS X
ABI on PowerPC/AltiVec processors - G4/G5 or IBM PPC 7400/7410/970. 
"""

import array
import sys

import corepy.spre.spe as spe
import ppc_exec
# from synnumeric import array_address

import corepy.arch.ppc.isa as ppc
import corepy.arch.vmx.isa as vmx
from   corepy.arch.ppc.lib.util import load_word

ExecParams = ppc_exec.ExecParams


# ------------------------------
# Registers
# ------------------------------

class GPRegister(spe.Register):
  def __init__(self, reg, code):
    spe.Register.__init__(self, reg, code, prefix = 'r')

class FPRegister(spe.Register):
  def __init__(self, reg, code):
    spe.Register.__init__(self, reg, code, prefix = 'f')

class VMXRegister(spe.Register): 
  def __init__(self, reg, code):
    spe.Register.__init__(self, reg, code, prefix = 'v')


# ------------------------------
# Constants
# ------------------------------

WORD_TYPE = 'I'           # array type that corresponds to 1 word
WORD_SIZE = 4             # size in bytes of one word
WORD_BITS = WORD_SIZE * 8 # number of bits in a word

# Parameter Registers
gp_param_1 = 3
gp_param_2 = 4
gp_param_3 = 5

# Return registers
# fp_return = FPRegister(1)
# vx_return = VMXRegister(1)
# gp_return = GPRegister(3)

# Callee save registers
gp_save = [GPRegister(i, None) for i in range(14, 32)]
fp_save = [FPRegister(i, None) for i in range(14, 32)]
vx_save = [VMXRegister(i, None) for i in range(20, 32)]


def copy_param(code, target, param):
  """
  Copy a parameter to the taget register.
  """
  if param not in (gp_param_1, gp_param_2, gp_param_3):
    raise Exception('Invalid parameter id: ' + str(param))
  code.add(ppc.addi(target, param, 0))
  return


# ------------------------------------------------------------
# InstructionStream
# ------------------------------------------------------------

class InstructionStream(spe.InstructionStream):
  """
  This implementation of InstructionStream conforms to the Mac OS X
  ABI for  32-bit PowerPC processors.
  
  An InstructionStream is the main abstraction for a sequence of
  instructions and the processor resources it uses.  The user can add
  arbitrary instructions to a stream using the add() method and
  execute then with the Processor.execute() method.  Instructions are
  executed starting with the first instruction added by the user.  An 
  instruction stream can return an integer or floating point value by
  placing the result in gp_return or fp_return and calling execute()
  with the appropriate return mode.  Any other values passed between
  the calling environment and the InstructionStream should be passed
  through memory.

  InstructionStream manages register allocation and also tracks heap
  storage to by its instructions.  Registers are 'allocated' to the
  user via requests to acquire_register(). When the user is done with
  the register, it must be released using release_register(). If not,
  it is unavailable for future use.  Advanced register allocation is
  left to the user.  If all available registers have been acquired, an
  exception is thrown.  Note that the return registers are included in
  the collection of available registers.

  If instructions use heap allocated memory (e.g., an array() to cache
  values during execution), they can pass a reference to
  InstructionStream using add_storage().  This assures that the memory
  will not be garbage collected until the InstructionStream has been
  cleared.  (note that this is an alternative to using the stack for
  temporary variables)

  Internally, the instruction stream is broken into three sections: a
  prologue, the code, and an epilogue.  The code section contains the
  user supplied instructions.  The prologue and epilogue manage
  register saves and any other ABI considerations. They are stored in
  separate memory locations and called immediately before (prologue)
  and after (epilogue) the user code.
  """

  # Class attributes

  # Register file descriptor: ('file id', register class, valid values)
  # These are used during instanciation to create register files for 
  # the InstructionStream instance.
  RegisterFiles = (('gp', GPRegister, range(2,10) + range(14, 31)),
                   ('fp', FPRegister, range(0,32)),
                   ('vector', VMXRegister, range(0,32)))

  default_register_type = GPRegister
  exec_module   = ppc_exec
  instruction_type  = WORD_TYPE

  def __init__(self):
    spe.InstructionStream.__init__(self)
    
    # Memory buffers for saved registers
    self._saved_gp_registers = None
    self._saved_fp_registers = None
    self._saved_vx_registers = None

    # Return Register 'Constants'
    #   *_return can be used with a return register is needed.

    #   Note that these do not reserve the register, but only identify
    #   the registers.  To reserve a return register, use:
    #     code.acquire_register(reg = code.gp_return)
    self.fp_return = FPRegister(1, self)
    self.vx_return = VMXRegister(1, self)
    self.gp_return = GPRegister(3, self)
    self._vrsave = GPRegister(31, self)

    return


  def make_executable(self):
    self.exec_module.make_executable(self.render_code.buffer_info()[0], len(self.render_code))
    return 

  def create_register_files(self):
    # Each declarative RegisterFiles entry is:
    #   (file_id, register class, valid values)
    for reg_type, cls, values in self.RegisterFiles:
      regs = [cls(value, self) for value in values]
      self._register_files[cls] = spe.RegisterFile(regs, reg_type)
      self._reg_type[reg_type] = cls
      for reg in regs:
        reg.code = self
    
    return
  
  # ------------------------------
  # Execute/ABI support
  # ------------------------------

  def _load_word(self, array, reg, word):
    """Load an immediate value into a register w/o using load_word(); instead
       append the instruction objects to an array.
       Used when synthesizing the prologue/epilogue."""
    array.append(ppc.addi(reg, 0, word & 0xFFFF, ignore_active = True))
    if (word & 0xFFFF) != word:
      array.append(ppc.addis(reg, reg, ((word + 32768) >> 16) & 0xFFFF, ignore_active = True))
    return

  def _synthesize_prologue(self):
    """
    Create the prologue. (see PPC ABI p41)

    This manages the register preservation requirements from the ABI.

    TODO: CR2-4 need to be preserved.
    """

    # Reset the prologue
    self._prologue = [self.lbl_prologue]

    # Get the lists of registers to save
    save_gp = [reg for reg in self._register_files[GPRegister].get_used() if reg in gp_save]
    save_fp = [reg for reg in self._register_files[FPRegister].get_used() if reg in fp_save]
    save_vx = [reg for reg in self._register_files[VMXRegister].get_used() if reg in vx_save]    
    
    self._saved_gp_registers = array.array('I', range(len(save_gp)))
    self._saved_fp_registers = array.array('d', range(len(save_fp)))
    self._saved_vx_registers = array.array('I', range(len(save_vx)*4))

    # Add the instructions to save the registers

    # Store the value in register 2 in the red zone
    #  r1 is the stackpointer, -4(r1) is in the red zone
    
    r_addr = GPRegister(13, None) # Only available volatile register
    r_idx = GPRegister(14, None)  # Non-volatile; safe to use before restoring

    self._load_word(self._prologue, r_addr, self._saved_gp_registers.buffer_info()[0])

    for i, reg in enumerate(save_gp):
      # print 'saving gp:', reg, 2, i * WORD_SIZE
      self._prologue.append(ppc.stw(reg, r_addr, i * WORD_SIZE, ignore_active = True))

    self._load_word(self._prologue, r_addr, self._saved_fp_registers.buffer_info()[0])
    
    for i, reg in enumerate(save_fp):
      # print 'saving fp:', reg, 2, i * WORD_SIZE
      self._prologue.append(ppc.stfd(reg, r_addr, i * WORD_SIZE * 2, ignore_active = True))

    self._load_word(self._prologue, r_addr, self._saved_vx_registers.buffer_info()[0])
    
    for i, reg in enumerate(save_vx):
      #print 'saving vx:', reg, 2, i * WORD_SIZE
      self._load_word(self._prologue, r_idx, i * WORD_SIZE * 4)
      self._prologue.append(vmx.stvx(reg, r_idx, r_addr, ignore_active = True))
      # print 'TODO: VMX Support'
      
    # Set up VRSAVE
    # Currently, we save the old value of VRSAVE in r31.
    # On the G4, someone stomps on registers < 20 ... save them all for now.

    # Save vrsave and put our value in it
    self._prologue.append(ppc.mfvrsave(self._vrsave, ignore_active = True))
    self._load_word(self._prologue, r_addr, 0xFFFFFFFF)
    self._prologue.append(ppc.mtvrsave(r_addr, ignore_active = True))    
    return


  def _synthesize_epilogue(self):
    """
    Save the values in some registers (see PPC ABI p41)
    """

    # Reset the epilogue
    self._epilogue = [self.lbl_epilogue]

    # Restore vrsave
    self._epilogue.append(ppc.mtvrsave(self._vrsave))

    # Get the list of saved registers
    save_gp = [reg for reg in self._register_files[GPRegister].get_used() if reg in gp_save]
    save_fp = [reg for reg in self._register_files[FPRegister].get_used() if reg in fp_save]
    save_vx = [reg for reg in self._register_files[VMXRegister].get_used() if reg in vx_save]    

    r_addr = GPRegister(13, None) # Only available volatile register
    r_idx = GPRegister(14, None)  # Non-volatile; safe to use before restoring

    self._load_word(self._epilogue, r_addr, self._saved_vx_registers.buffer_info()[0])

    for i, reg in enumerate(save_vx):
      # print 'restoring vx:', reg, r_addr, i * WORD_SIZE
      self._load_word(self._epilogue, r_dx, i * WORD_SIZE * 4)
      self._epilogue.add(vmx.lvx(reg, r_idx, r_addr, ignore_active = True))

    self._load_word(self._epilogue, r_addr, self._saved_fp_registers.buffer_info()[0])

    for i, reg in enumerate(save_fp):
      # print 'restoring fp:', reg, r_addr, i * WORD_SIZE
      self._epilogue.append(ppc.lfd(reg, r_addr, i * WORD_SIZE * 2, ignore_active = True))

    self._load_word(self._epilogue, r_addr, self._saved_gp_registers.buffer_info()[0])

    for i, reg in enumerate(save_gp):
      # print 'restoring gp:', reg, r_addr, i * WORD_SIZE
      self._epilogue.append(ppc.lwz(reg, r_addr, i * WORD_SIZE, ignore_active = True))

    self._epilogue.append(ppc.blr(ignore_active = True))
    return


class Processor(spe.Processor):
  exec_module = ppc_exec
  

# ------------------------------------------------------------
# Unit tests
# ------------------------------------------------------------

def TestInt():
  code = InstructionStream()
  proc = Processor()

  code.add(ppc.addi(code.gp_return, 0, 12))

  r = proc.execute(code, debug=True)
  assert(r == 12)
  print 'int result:', r
  return

def TestFloat():
  code = InstructionStream()
  proc = Processor()
  a = array.array('d', [3.14])

  load_word(code, gp_return, a.buffer_info()[0])
  code.add(ppc.lfd(code.fp_return, code.gp_return, 0))

  r = proc.execute(code, mode='fp', debug=True)
  assert(r == 3.14)
  print 'float result:', r
  return

def TestExtended():

  class Add10(spe.ExtendedInstruction):
    isa_module = ppc
    def __init__(self, d, value):
      self.d = d
      self.value = value

      spe.ExtendedInstruction.__init__(self)
      
      return

    def block(self):
      for i in range(10):
        ppc.addi(self.d, self.d, self.value)
      return
  
  code = InstructionStream()
  proc = Processor()

  # Using code.add 
  code.add(ppc.addi(code.gp_return, 0, 0))
  code.add(Add10(code.gp_return, 1))

  Add10.ex(1).eval(code, reg = code.gp_return)
  
  code.print_code()
  r = proc.execute(code)
  print r
  assert(r == 20)

  # Using active code
  code.reset()
  ppc.set_active_code(code)

  ppc.addi(code.gp_return, 0, 0)  
  Add10(code.gp_return, 1)

  Add10.ex(1).eval(ppc.get_active_code(), reg = code.gp_return)
  
  code.print_code()
  r = proc.execute(code)
  print r
  assert(r == 20)

  
  return


def TestCodedCall():
  code = InstructionStream()
  proc = Processor()
  
  a = array.array('d', [3.14])

  load_word(code, code.gp_return, a.buffer_info()[0])

  ppc.set_active_code(code)
  ppc.lfd(code.fp_return, code.gp_return, 0)
  code.print_code()
  r = proc.execute(code, mode='fp', debug=True)
  assert(r == 3.14)
  print 'float result:', r
  return


if __name__ == '__main__':
  # TestInt()
  # TestFloat()
  # TestCodedCall()
  TestExtended()
