# XeonE7Msr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.XeonE7Msr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_XEON_E7_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x2F
           )

MSR_XEON_E7_FEATURE_CONFIG  = 0x0000013C

class MSR_XEON_E7_FEATURE_CONFIG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("AESConfiguration",    UINT32, 2),
    ("Reserved1",           UINT32, 30),
    ("Reserved2",           UINT32, 32)
  ]

class MSR_XEON_E7_FEATURE_CONFIG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_E7_FEATURE_CONFIG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_E7_OFFCORE_RSP_1        = 0x000001A7
MSR_XEON_E7_TURBO_RATIO_LIMIT    = 0x000001AD

MSR_XEON_E7_C8_PMON_BOX_CTRL     = 0x00000F40
MSR_XEON_E7_C8_PMON_BOX_STATUS   = 0x00000F41
MSR_XEON_E7_C8_PMON_BOX_OVF_CTRL = 0x00000F42

MSR_XEON_E7_C8_PMON_EVNT_SEL0  = 0x00000F50
MSR_XEON_E7_C8_PMON_EVNT_SEL1  = 0x00000F52
MSR_XEON_E7_C8_PMON_EVNT_SEL2  = 0x00000F54
MSR_XEON_E7_C8_PMON_EVNT_SEL3  = 0x00000F56
MSR_XEON_E7_C8_PMON_EVNT_SEL4  = 0x00000F58
MSR_XEON_E7_C8_PMON_EVNT_SEL5  = 0x00000F5A

MSR_XEON_E7_C8_PMON_CTR0  = 0x00000F51
MSR_XEON_E7_C8_PMON_CTR1  = 0x00000F53
MSR_XEON_E7_C8_PMON_CTR2  = 0x00000F55
MSR_XEON_E7_C8_PMON_CTR3  = 0x00000F57
MSR_XEON_E7_C8_PMON_CTR4  = 0x00000F59
MSR_XEON_E7_C8_PMON_CTR5  = 0x00000F5B

MSR_XEON_E7_C9_PMON_BOX_CTRL      = 0x00000FC0
MSR_XEON_E7_C9_PMON_BOX_STATUS    = 0x00000FC1
MSR_XEON_E7_C9_PMON_BOX_OVF_CTRL  = 0x00000FC2

MSR_XEON_E7_C9_PMON_EVNT_SEL0  = 0x00000FD0
MSR_XEON_E7_C9_PMON_EVNT_SEL1  = 0x00000FD2
MSR_XEON_E7_C9_PMON_EVNT_SEL2  = 0x00000FD4
MSR_XEON_E7_C9_PMON_EVNT_SEL3  = 0x00000FD6
MSR_XEON_E7_C9_PMON_EVNT_SEL4  = 0x00000FD8
MSR_XEON_E7_C9_PMON_EVNT_SEL5  = 0x00000FDA

MSR_XEON_E7_C9_PMON_CTR0  = 0x00000FD1
MSR_XEON_E7_C9_PMON_CTR1  = 0x00000FD3
MSR_XEON_E7_C9_PMON_CTR2  = 0x00000FD5
MSR_XEON_E7_C9_PMON_CTR3  = 0x00000FD7
MSR_XEON_E7_C9_PMON_CTR4  = 0x00000FD9
MSR_XEON_E7_C9_PMON_CTR5  = 0x00000FDB
