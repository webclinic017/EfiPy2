# Acpi30.py
#
# EfiPy2.MdePkg.IndustryStandard.Acpi30
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.Acpi20 import *

ACPI_LARGE_EXTENDED_ADDRESS_SPACE_DESCRIPTOR_NAME    = 0x0B

ACPI_EXTENDED_ADDRESS_SPACE_DESCRIPTOR    = 0x8B

class EFI_ACPI_EXTENDED_ADDRESS_SPACE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                ACPI_LARGE_RESOURCE_HEADER),
    ("ResType",               UINT8),
    ("GenFlag",               UINT8),
    ("SpecificFlag",          UINT8),
    ("RevisionId",            UINT8),
    ("Reserved",              UINT8),
    ("AddrSpaceGranularity",  UINT64),
    ("AddrRangeMin",          UINT64),
    ("AddrRangeMax",          UINT64),
    ("AddrTranslationOffset", UINT64),
    ("AddrLen",               UINT64),
    ("TypeSpecificAttribute", UINT64)
  ]

EFI_ACPI_MEMORY_TYPE_SPECIFIC_ATTRIBUTES_UC  = 0x0000000000000001
EFI_ACPI_MEMORY_TYPE_SPECIFIC_ATTRIBUTES_WC  = 0x0000000000000002
EFI_ACPI_MEMORY_TYPE_SPECIFIC_ATTRIBUTES_WT  = 0x0000000000000004
EFI_ACPI_MEMORY_TYPE_SPECIFIC_ATTRIBUTES_WB  = 0x0000000000000008
EFI_ACPI_MEMORY_TYPE_SPECIFIC_ATTRIBUTES_UCE = 0x0000000000000010
EFI_ACPI_MEMORY_TYPE_SPECIFIC_ATTRIBUTES_NV  = 0x0000000000008000

class EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AddressSpaceId",    UINT8),
    ("RegisterBitWidth",  UINT8),
    ("RegisterBitOffset", UINT8),
    ("AccessSize",        UINT8),
    ("Address",           UINT64)
  ]

EFI_ACPI_3_0_SYSTEM_MEMORY              = 0
EFI_ACPI_3_0_SYSTEM_IO                  = 1
EFI_ACPI_3_0_PCI_CONFIGURATION_SPACE    = 2
EFI_ACPI_3_0_EMBEDDED_CONTROLLER        = 3
EFI_ACPI_3_0_SMBUS                      = 4
EFI_ACPI_3_0_FUNCTIONAL_FIXED_HARDWARE  = 0x7F

EFI_ACPI_3_0_UNDEFINED  = 0
EFI_ACPI_3_0_BYTE       = 1
EFI_ACPI_3_0_WORD       = 2
EFI_ACPI_3_0_DWORD      = 3
EFI_ACPI_3_0_QWORD      = 4

EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_POINTER = EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER

EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_POINTER_REVISION = 0x02

EFI_ACPI_3_0_COMMON_HEADER = EFI_ACPI_2_0_COMMON_HEADER

EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_3_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

class EFI_ACPI_3_0_FIXED_ACPI_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_ACPI_DESCRIPTION_HEADER),
    ("FirmwareCtrl",      UINT32),
    ("Dsdt",              UINT32),
    ("Reserved0",         UINT8),
    ("PreferredPmProfile",UINT8),
    ("SciInt",            UINT16),
    ("SmiCmd",            UINT32),
    ("AcpiEnable",        UINT8),
    ("AcpiDisable",       UINT8),
    ("S4BiosReq",         UINT8),
    ("PstateCnt",         UINT8),
    ("Pm1aEvtBlk",        UINT32),
    ("Pm1bEvtBlk",        UINT32),
    ("Pm1aCntBlk",        UINT32),
    ("Pm1bCntBlk",        UINT32),
    ("Pm2CntBlk",         UINT32),
    ("PmTmrBlk",          UINT32),
    ("Gpe0Blk",           UINT32),
    ("Gpe1Blk",           UINT32),
    ("Pm1EvtLen",         UINT8),
    ("Pm1CntLen",         UINT8),
    ("Pm2CntLen",         UINT8),
    ("PmTmrLen",          UINT8),
    ("Gpe0BlkLen",        UINT8),
    ("Gpe1BlkLen",        UINT8),
    ("Gpe1Base",          UINT8),
    ("CstCnt",            UINT8),
    ("PLvl2Lat",          UINT16),
    ("PLvl3Lat",          UINT16),
    ("FlushSize",         UINT16),
    ("FlushStride",       UINT16),
    ("DutyOffset",        UINT8),
    ("DutyWidth",         UINT8),
    ("DayAlrm",           UINT8),
    ("MonAlrm",           UINT8),
    ("Century",           UINT8),
    ("IaPcBootArch",      UINT16),
    ("Reserved1",         UINT8),
    ("Flags",             UINT32),
    ("ResetReg",          EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("ResetValue",        UINT8),
    ("Reserved2",         UINT8 * 3),
    ("XFirmwareCtrl",     UINT64),
    ("XDsdt",             UINT64),
    ("XPm1aEvtBlk",       EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1bEvtBlk",       EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1aCntBlk",       EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1bCntBlk",       EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm2CntBlk",        EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPmTmrBlk",         EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("XGpe0Blk",          EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("XGpe1Blk",          EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE)
  ]

EFI_ACPI_3_0_FIXED_ACPI_DESCRIPTION_TABLE_REVISION  = 0x04

EFI_ACPI_3_0_PM_PROFILE_UNSPECIFIED         = 0
EFI_ACPI_3_0_PM_PROFILE_DESKTOP             = 1
EFI_ACPI_3_0_PM_PROFILE_MOBILE              = 2
EFI_ACPI_3_0_PM_PROFILE_WORKSTATION         = 3
EFI_ACPI_3_0_PM_PROFILE_ENTERPRISE_SERVER   = 4
EFI_ACPI_3_0_PM_PROFILE_SOHO_SERVER         = 5
EFI_ACPI_3_0_PM_PROFILE_APPLIANCE_PC        = 6
EFI_ACPI_3_0_PM_PROFILE_PERFORMANCE_SERVER  = 7

EFI_ACPI_3_0_LEGACY_DEVICES              = BIT0
EFI_ACPI_3_0_8042                        = BIT1
EFI_ACPI_3_0_VGA_NOT_PRESENT             = BIT2
EFI_ACPI_3_0_MSI_NOT_SUPPORTED           = BIT3
EFI_ACPI_3_0_PCIE_ASPM_CONTROLS          = BIT4

EFI_ACPI_3_0_WBINVD                                 = BIT0
EFI_ACPI_3_0_WBINVD_FLUSH                           = BIT1
EFI_ACPI_3_0_PROC_C1                                = BIT2
EFI_ACPI_3_0_P_LVL2_UP                              = BIT3
EFI_ACPI_3_0_PWR_BUTTON                             = BIT4
EFI_ACPI_3_0_SLP_BUTTON                             = BIT5
EFI_ACPI_3_0_FIX_RTC                                = BIT6
EFI_ACPI_3_0_RTC_S4                                 = BIT7
EFI_ACPI_3_0_TMR_VAL_EXT                            = BIT8
EFI_ACPI_3_0_DCK_CAP                                = BIT9
EFI_ACPI_3_0_RESET_REG_SUP                          = BIT10
EFI_ACPI_3_0_SEALED_CASE                            = BIT11
EFI_ACPI_3_0_HEADLESS                               = BIT12
EFI_ACPI_3_0_CPU_SW_SLP                             = BIT13
EFI_ACPI_3_0_PCI_EXP_WAK                            = BIT14
EFI_ACPI_3_0_USE_PLATFORM_CLOCK                     = BIT15
EFI_ACPI_3_0_S4_RTC_STS_VALID                       = BIT16
EFI_ACPI_3_0_REMOTE_POWER_ON_CAPABLE                = BIT17
EFI_ACPI_3_0_FORCE_APIC_CLUSTER_MODEL               = BIT18
EFI_ACPI_3_0_FORCE_APIC_PHYSICAL_DESTINATION_MODE   = BIT19

EFI_ACPI_3_0_FIRMWARE_ACPI_CONTROL_STRUCTURE = EFI_ACPI_2_0_FIRMWARE_ACPI_CONTROL_STRUCTURE

EFI_ACPI_3_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_VERSION  = 0x01

EFI_ACPI_3_0_S4BIOS_F       = BIT0

EFI_ACPI_3_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_REVISION   = 0x02
EFI_ACPI_3_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_REVISION        = 0x02

class EFI_ACPI_3_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_ACPI_DESCRIPTION_HEADER),
    ("LocalApicAddress",  UINT32),
    ("Flags",             UINT32)
  ]

EFI_ACPI_3_0_MULTIPLE_APIC_DESCRIPTION_TABLE_REVISION = 0x02

EFI_ACPI_3_0_PCAT_COMPAT         = BIT0

EFI_ACPI_3_0_PROCESSOR_LOCAL_APIC           = 0x00
EFI_ACPI_3_0_IO_APIC                        = 0x01
EFI_ACPI_3_0_INTERRUPT_SOURCE_OVERRIDE      = 0x02
EFI_ACPI_3_0_NON_MASKABLE_INTERRUPT_SOURCE  = 0x03
EFI_ACPI_3_0_LOCAL_APIC_NMI                 = 0x04
EFI_ACPI_3_0_LOCAL_APIC_ADDRESS_OVERRIDE    = 0x05
EFI_ACPI_3_0_IO_SAPIC                       = 0x06
EFI_ACPI_3_0_LOCAL_SAPIC                    = 0x07
EFI_ACPI_3_0_PLATFORM_INTERRUPT_SOURCES     = 0x08

EFI_ACPI_3_0_PROCESSOR_LOCAL_APIC_STRUCTURE = EFI_ACPI_2_0_PROCESSOR_LOCAL_APIC_STRUCTURE

EFI_ACPI_3_0_LOCAL_APIC_ENABLED        = BIT0

EFI_ACPI_3_0_IO_APIC_STRUCTURE = EFI_ACPI_2_0_IO_APIC_STRUCTURE

EFI_ACPI_3_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE = EFI_ACPI_2_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE

class EFI_ACPI_3_0_PLATFORM_INTERRUPT_APIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT8),
    ("Length",                        UINT8),
    ("Flags",                         UINT16),
    ("InterruptType",                 UINT8),
    ("ProcessorId",                   UINT8),
    ("ProcessorEid",                  UINT8),
    ("IoSapicVector",                 UINT8),
    ("GlobalSystemInterrupt",         UINT32),
    ("PlatformInterruptSourceFlags",  UINT32),
    ("CpeiProcessorOverride",         UINT8),
    ("Reserved",                      UINT8 * 31)
  ]

EFI_ACPI_3_0_POLARITY      = (3 << 0)
EFI_ACPI_3_0_TRIGGER_MODE  = (3 << 2)

EFI_ACPI_3_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE = EFI_ACPI_2_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE

EFI_ACPI_3_0_LOCAL_APIC_NMI_STRUCTURE = EFI_ACPI_2_0_LOCAL_APIC_NMI_STRUCTURE

EFI_ACPI_3_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE = EFI_ACPI_2_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE

EFI_ACPI_3_0_IO_SAPIC_STRUCTURE = EFI_ACPI_2_0_IO_SAPIC_STRUCTURE

EFI_ACPI_3_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE = EFI_ACPI_2_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE

class EFI_ACPI_3_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT8),
    ("Length",                        UINT8),
    ("Flags",                         UINT16),
    ("InterruptType",                 UINT8),
    ("ProcessorId",                   UINT8),
    ("ProcessorEid",                  UINT8),
    ("IoSapicVector",                 UINT8),
    ("GlobalSystemInterrupt",         UINT32),
    ("PlatformInterruptSourceFlags",  UINT32)
  ]

EFI_ACPI_3_0_CPEI_PROCESSOR_OVERRIDE          = BIT0

EFI_ACPI_3_0_SMART_BATTERY_DESCRIPTION_TABLE = EFI_ACPI_2_0_SMART_BATTERY_DESCRIPTION_TABLE

EFI_ACPI_3_0_SMART_BATTERY_DESCRIPTION_TABLE_REVISION = 0x01

class EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_ACPI_DESCRIPTION_HEADER),
    ("EcControl", EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("EcData",    EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("Uid",       UINT32),
    ("GpeBit",    UINT8)
  ]

EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION  = 0x01

class EFI_ACPI_3_0_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved1", UINT32),
    ("Reserved2", UINT64)
  ]

EFI_ACPI_3_0_SYSTEM_RESOURCE_AFFINITY_TABLE_REVISION  = 0x02

EFI_ACPI_3_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY  = 0x00
EFI_ACPI_3_0_MEMORY_AFFINITY                      = 0x01

class EFI_ACPI_3_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                  UINT8),
    ("Length",                UINT8),
    ("ProximityDomain7To0",   UINT8),
    ("ApicId",                UINT8),
    ("Flags",                 UINT32),
    ("LocalSapicEid",         UINT8),
    ("ProximityDomain31To8",  UINT8 * 3),
    ("Reserved",              UINT8 * 4)
  ]

EFI_ACPI_3_0_PROCESSOR_LOCAL_APIC_SAPIC_ENABLED = (1 << 0)

class EFI_ACPI_3_0_MEMORY_AFFINITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("ProximityDomain", UINT32),
    ("Reserved1",       UINT16),
    ("AddressBaseLow",  UINT32),
    ("AddressBaseHigh", UINT32),
    ("LengthLow",       UINT32),
    ("LengthHigh",      UINT32),
    ("Reserved2",       UINT32),
    ("Flags",           UINT32),
    ("Reserved3",       UINT64)
  ]

EFI_ACPI_3_0_MEMORY_ENABLED       = (1 << 0)
EFI_ACPI_3_0_MEMORY_HOT_PLUGGABLE = (1 << 1)
EFI_ACPI_3_0_MEMORY_NONVOLATILE   = (1 << 2)

class EFI_ACPI_3_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                    EFI_ACPI_DESCRIPTION_HEADER),
    ("NumberOfSystemLocalities",  UINT64)
  ]

EFI_ACPI_3_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_REVISION  = 0x01

EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE  = EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE
EFI_ACPI_3_0_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_MULTIPLE_SAPIC_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_3_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE  = SIGNATURE_32('E', 'C', 'D', 'T')
EFI_ACPI_3_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_3_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE  = EFI_ACPI_2_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE
EFI_ACPI_3_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_3_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE  = EFI_ACPI_2_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE
EFI_ACPI_3_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE  = EFI_ACPI_2_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE
EFI_ACPI_3_0_SYSTEM_RESOURCE_AFFINITY_TABLE_SIGNATURE  = EFI_ACPI_2_0_STATIC_RESOURCE_AFFINITY_TABLE_SIGNATURE
EFI_ACPI_3_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_3_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_3_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE  = EFI_ACPI_2_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE
EFI_ACPI_3_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE  = SIGNATURE_32('C', 'P', 'E', 'P')
EFI_ACPI_3_0_DEBUG_PORT_TABLE_SIGNATURE  = EFI_ACPI_2_0_DEBUG_PORT_TABLE_SIGNATURE
EFI_ACPI_3_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_3_0_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE  = SIGNATURE_32('H', 'P', 'E', 'T')
EFI_ACPI_3_0_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('M', 'C', 'F', 'G')
EFI_ACPI_3_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE  = EFI_ACPI_2_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE
EFI_ACPI_3_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE  = EFI_ACPI_2_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_SIGNATURE
EFI_ACPI_3_0_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE  = SIGNATURE_32('T', 'C', 'P', 'A')
EFI_ACPI_3_0_WATCHDOG_RESOURCE_TABLE_SIGNATURE  = SIGNATURE_32('W', 'D', 'R', 'T')
EFI_ACPI_3_0_WATCHDOG_ACTION_TABLE_SIGNATURE  = SIGNATURE_32('W', 'D', 'A', 'T')
EFI_ACPI_3_0_WINDOWS_SPECIFIC_PROPERTIES_TABLE_SIGNATURE  = SIGNATURE_32('W', 'S', 'P', 'T')
EFI_ACPI_3_0_ISCSI_BOOT_FIRMWARE_TABLE_SIGNATURE  = SIGNATURE_32('i', 'B', 'F', 'T')
