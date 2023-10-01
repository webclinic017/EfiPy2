# PiMultiPhase.py
#
# EfiPy2.MdePkg.Pi.PiMultiPhase
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def DXE_ERROR(StatusCode):
  return MAX_BIT | (MAX_BIT >> 2) | StatusCode

EFI_REQUEST_UNLOAD_IMAGE  = DXE_ERROR (1)

EFI_NOT_AVAILABLE_YET     = DXE_ERROR (2)

def PI_ENCODE_WARNING(a):
  return (MAX_BIT >> 2) | a

def PI_ENCODE_ERROR(a):
  return MAX_BIT | (MAX_BIT >> 2) | a

EFI_INTERRUPT_PENDING               = PI_ENCODE_ERROR (0)

EFI_WARN_INTERRUPT_SOURCE_PENDING   = PI_ENCODE_WARNING (0)
EFI_WARN_INTERRUPT_SOURCE_QUIESCED  = PI_ENCODE_WARNING (1)

EFI_AUTH_STATUS_PLATFORM_OVERRIDE   = 0x01
EFI_AUTH_STATUS_IMAGE_SIGNED        = 0x02
EFI_AUTH_STATUS_NOT_TESTED          = 0x04
EFI_AUTH_STATUS_TEST_FAILED         = 0x08
EFI_AUTH_STATUS_ALL                 = 0x0f

EFI_MMRAM_OPEN                = 0x00000001
EFI_MMRAM_CLOSED              = 0x00000002
EFI_MMRAM_LOCKED              = 0x00000004
EFI_CACHEABLE                 = 0x00000008
EFI_ALLOCATED                 = 0x00000010
EFI_NEEDS_TESTING             = 0x00000020
EFI_NEEDS_ECC_INITIALIZATION  = 0x00000040

EFI_SMRAM_OPEN    = EFI_MMRAM_OPEN
EFI_SMRAM_CLOSED  = EFI_MMRAM_CLOSED
EFI_SMRAM_LOCKED  = EFI_MMRAM_LOCKED

class EFI_MMRAM_DESCRIPTOR (Structure):
  _fields_ = [
    ("PhysicalStart", EFI_PHYSICAL_ADDRESS),
    ("CpuStart",      EFI_PHYSICAL_ADDRESS),  
    ("PhysicalSize",  UINT64),
    ("RegionState",   UINT64)
  ]

EFI_SMRAM_DESCRIPTOR = EFI_MMRAM_DESCRIPTOR

class EFI_MM_RESERVED_MMRAM_REGION (Structure):
  _fields_ = [
    ("MmramReservedStart",  EFI_PHYSICAL_ADDRESS),
    ("MmramReservedSize",   UINT64)
  ]

EFI_PCD_TYPE_8    = 0
EFI_PCD_TYPE_16   = 1
EFI_PCD_TYPE_32   = 2
EFI_PCD_TYPE_64   = 3
EFI_PCD_TYPE_BOOL = 4
EFI_PCD_TYPE_PTR  = 5
EFI_PCD_TYPE      = ENUM

class EFI_PCD_INFO (Structure):
  _fields_ = [
    ("PcdType", EFI_PCD_TYPE),
    ("PcdSize", UINTN),
    ("PcdName", PCHAR8)
  ]

EFI_AP_PROCEDURE = CFUNCTYPE (
  VOID,
  PVOID # IN  OUT *Buffer
  )

EFI_AP_PROCEDURE2 = CFUNCTYPE (
  EFI_STATUS,
  PVOID # IN  *ProcedureArgument
  )

