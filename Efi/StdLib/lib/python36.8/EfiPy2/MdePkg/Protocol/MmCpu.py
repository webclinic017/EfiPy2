# MmCpu.py
#
# EfiPy2.MdePkg.Protocol.MmCpu
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiMmCpuProtocolGuid = \
  EFI_GUID (0xeb346b97, 0x975f, 0x4a9f, ( 0x8b, 0x22, 0xf8, 0xe9, 0x2b, 0xb3, 0xd5, 0x69 ))

EFI_MM_SAVE_STATE_REGISTER_GDTBASE    = 4
EFI_MM_SAVE_STATE_REGISTER_IDTBASE    = 5
EFI_MM_SAVE_STATE_REGISTER_LDTBASE    = 6
EFI_MM_SAVE_STATE_REGISTER_GDTLIMIT   = 7
EFI_MM_SAVE_STATE_REGISTER_IDTLIMIT   = 8
EFI_MM_SAVE_STATE_REGISTER_LDTLIMIT   = 9
EFI_MM_SAVE_STATE_REGISTER_LDTINFO    = 10
EFI_MM_SAVE_STATE_REGISTER_ES         = 20
EFI_MM_SAVE_STATE_REGISTER_CS         = 21
EFI_MM_SAVE_STATE_REGISTER_SS         = 22
EFI_MM_SAVE_STATE_REGISTER_DS         = 23
EFI_MM_SAVE_STATE_REGISTER_FS         = 24
EFI_MM_SAVE_STATE_REGISTER_GS         = 25
EFI_MM_SAVE_STATE_REGISTER_LDTR_SEL   = 26
EFI_MM_SAVE_STATE_REGISTER_TR_SEL     = 27
EFI_MM_SAVE_STATE_REGISTER_DR7        = 28
EFI_MM_SAVE_STATE_REGISTER_DR6        = 29
EFI_MM_SAVE_STATE_REGISTER_R8         = 30
EFI_MM_SAVE_STATE_REGISTER_R9         = 31
EFI_MM_SAVE_STATE_REGISTER_R10        = 32
EFI_MM_SAVE_STATE_REGISTER_R11        = 33
EFI_MM_SAVE_STATE_REGISTER_R12        = 34
EFI_MM_SAVE_STATE_REGISTER_R13        = 35
EFI_MM_SAVE_STATE_REGISTER_R14        = 36
EFI_MM_SAVE_STATE_REGISTER_R15        = 37
EFI_MM_SAVE_STATE_REGISTER_RAX        = 38
EFI_MM_SAVE_STATE_REGISTER_RBX        = 39
EFI_MM_SAVE_STATE_REGISTER_RCX        = 40
EFI_MM_SAVE_STATE_REGISTER_RDX        = 41
EFI_MM_SAVE_STATE_REGISTER_RSP        = 42
EFI_MM_SAVE_STATE_REGISTER_RBP        = 43
EFI_MM_SAVE_STATE_REGISTER_RSI        = 44
EFI_MM_SAVE_STATE_REGISTER_RDI        = 45
EFI_MM_SAVE_STATE_REGISTER_RIP        = 46
EFI_MM_SAVE_STATE_REGISTER_RFLAGS     = 51
EFI_MM_SAVE_STATE_REGISTER_CR0        = 52
EFI_MM_SAVE_STATE_REGISTER_CR3        = 53
EFI_MM_SAVE_STATE_REGISTER_CR4        = 54
EFI_MM_SAVE_STATE_REGISTER_FCW        = 256
EFI_MM_SAVE_STATE_REGISTER_FSW        = 257
EFI_MM_SAVE_STATE_REGISTER_FTW        = 258
EFI_MM_SAVE_STATE_REGISTER_OPCODE     = 259
EFI_MM_SAVE_STATE_REGISTER_FP_EIP     = 260
EFI_MM_SAVE_STATE_REGISTER_FP_CS      = 261
EFI_MM_SAVE_STATE_REGISTER_DATAOFFSET = 262
EFI_MM_SAVE_STATE_REGISTER_FP_DS      = 263
EFI_MM_SAVE_STATE_REGISTER_MM0        = 264
EFI_MM_SAVE_STATE_REGISTER_MM1        = 265
EFI_MM_SAVE_STATE_REGISTER_MM2        = 266
EFI_MM_SAVE_STATE_REGISTER_MM3        = 267
EFI_MM_SAVE_STATE_REGISTER_MM4        = 268
EFI_MM_SAVE_STATE_REGISTER_MM5        = 269
EFI_MM_SAVE_STATE_REGISTER_MM6        = 270
EFI_MM_SAVE_STATE_REGISTER_MM7        = 271
EFI_MM_SAVE_STATE_REGISTER_XMM0       = 272
EFI_MM_SAVE_STATE_REGISTER_XMM1       = 273
EFI_MM_SAVE_STATE_REGISTER_XMM2       = 274
EFI_MM_SAVE_STATE_REGISTER_XMM3       = 275
EFI_MM_SAVE_STATE_REGISTER_XMM4       = 276
EFI_MM_SAVE_STATE_REGISTER_XMM5       = 277
EFI_MM_SAVE_STATE_REGISTER_XMM6       = 278
EFI_MM_SAVE_STATE_REGISTER_XMM7       = 279
EFI_MM_SAVE_STATE_REGISTER_XMM8       = 280
EFI_MM_SAVE_STATE_REGISTER_XMM9       = 281
EFI_MM_SAVE_STATE_REGISTER_XMM10      = 282
EFI_MM_SAVE_STATE_REGISTER_XMM11      = 283
EFI_MM_SAVE_STATE_REGISTER_XMM12      = 284
EFI_MM_SAVE_STATE_REGISTER_XMM13      = 285
EFI_MM_SAVE_STATE_REGISTER_XMM14      = 286
EFI_MM_SAVE_STATE_REGISTER_XMM15      = 287
EFI_MM_SAVE_STATE_REGISTER_IO           = 512
EFI_MM_SAVE_STATE_REGISTER_LMA          = 513
EFI_MM_SAVE_STATE_REGISTER_PROCESSOR_ID = 514
EFI_MM_SAVE_STATE_REGISTER              = ENUM

EFI_MM_SAVE_STATE_REGISTER_LMA_32BIT  = 32
EFI_MM_SAVE_STATE_REGISTER_LMA_64BIT  = 64

EFI_MM_SAVE_STATE_IO_WIDTH_UINT8  = 0
EFI_MM_SAVE_STATE_IO_WIDTH_UINT16 = 1
EFI_MM_SAVE_STATE_IO_WIDTH_UINT32 = 2
EFI_MM_SAVE_STATE_IO_WIDTH_UINT64 = 3
EFI_MM_SAVE_STATE_IO_WIDTH        = ENUM

EFI_MM_SAVE_STATE_IO_TYPE_INPUT      = 1
EFI_MM_SAVE_STATE_IO_TYPE_OUTPUT     = 2
EFI_MM_SAVE_STATE_IO_TYPE_STRING     = 4
EFI_MM_SAVE_STATE_IO_TYPE_REP_PREFIX = 8
EFI_MM_SAVE_STATE_IO_TYPE            = ENUM

class EFI_MM_SAVE_STATE_IO_INFO (Structure):
  _fields_ = [
    ("IoData",  UINT64),
    ("IoPort",  UINT16),
    ("IoWidth", EFI_MM_SAVE_STATE_IO_WIDTH),
    ("IoType",  EFI_MM_SAVE_STATE_IO_TYPE)
  ]

class EFI_MM_CPU_PROTOCOL (Structure):
  pass

EFI_MM_READ_SAVE_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_CPU_PROTOCOL), #   IN  CONST   *This,
  UINTN,                        #   IN          Width,
  EFI_MM_SAVE_STATE_REGISTER,   #   IN          Register,
  UINTN,                        #   IN          CpuIndex,
  PVOID                         #   OUT         *Buffer
  )

EFI_MM_WRITE_SAVE_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_CPU_PROTOCOL), #   IN  CONST   *This,
  UINTN,                        #   IN          Width,
  EFI_MM_SAVE_STATE_REGISTER,   #   IN          Register,
  UINTN,                        #   IN          CpuIndex,
  PVOID                         #   IN CONST    *Buffer
  )

EFI_MM_CPU_PROTOCOL._fields_ = [
    ("ReadSaveState",   EFI_MM_READ_SAVE_STATE),
    ("WriteSaveState",  EFI_MM_WRITE_SAVE_STATE)
  ]

