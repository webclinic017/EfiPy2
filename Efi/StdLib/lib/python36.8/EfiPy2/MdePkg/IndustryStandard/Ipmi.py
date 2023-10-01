# Ipmi.py
#
# EfiPy2.MdePkg.IndustryStandard.Ipmi
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.IpmiNetFnChassis         import *
from EfiPy2.MdePkg.IndustryStandard.IpmiNetFnBridge          import *
from EfiPy2.MdePkg.IndustryStandard.IpmiNetFnSensorEvent     import *
from EfiPy2.MdePkg.IndustryStandard.IpmiNetFnApp             import *
from EfiPy2.MdePkg.IndustryStandard.IpmiNetFnFirmware        import *
from EfiPy2.MdePkg.IndustryStandard.IpmiNetFnStorage         import *
from EfiPy2.MdePkg.IndustryStandard.IpmiNetFnTransport       import *
from EfiPy2.MdePkg.IndustryStandard.IpmiNetFnGroupExtension  import *

from EfiPy2.MdePkg.IndustryStandard.IpmiFruInformationStorage   import *

IPMI_COMP_CODE_NORMAL                           = 0x00
IPMI_COMP_CODE_NODE_BUSY                        = 0xC0
IPMI_COMP_CODE_INVALID_COMMAND                  = 0xC1
IPMI_COMP_CODE_INVALID_FOR_GIVEN_LUN            = 0xC2
IPMI_COMP_CODE_TIMEOUT                          = 0xC3
IPMI_COMP_CODE_OUT_OF_SPACE                     = 0xC4
IPMI_COMP_CODE_RESERVATION_CANCELED_OR_INVALID  = 0xC5
IPMI_COMP_CODE_REQUEST_DATA_TRUNCATED           = 0xC6
IPMI_COMP_CODE_INVALID_REQUEST_DATA_LENGTH      = 0xC7
IPMI_COMP_CODE_REQUEST_EXCEED_LIMIT             = 0xC8
IPMI_COMP_CODE_OUT_OF_RANGE                     = 0xC9
IPMI_COMP_CODE_CANNOT_RETURN                    = 0xCA
IPMI_COMP_CODE_NOT_PRESENT                      = 0xCB
IPMI_COMP_CODE_INVALID_DATA_FIELD               = 0xCC
IPMI_COMP_CODE_COMMAND_ILLEGAL                  = 0xCD
IPMI_COMP_CODE_CMD_RESP_NOT_PROVIDED            = 0xCE
IPMI_COMP_CODE_FAIL_DUP_REQUEST                 = 0xCF
IPMI_COMP_CODE_SDR_REP_IN_UPDATE_MODE           = 0xD0
IPMI_COMP_CODE_DEV_IN_FW_UPDATE_MODE            = 0xD1
IPMI_COMP_CODE_BMC_INIT_IN_PROGRESS             = 0xD2
IPMI_COMP_CODE_DEST_UNAVAILABLE                 = 0xD3
IPMI_COMP_CODE_INSUFFICIENT_PRIVILEGE           = 0xD4
IPMI_COMP_CODE_UNSUPPORTED_IN_PRESENT_STATE     = 0xD5
IPMI_COMP_CODE_SUBFUNCTION_DISABLED             = 0xD6
IPMI_COMP_CODE_UNSPECIFIED                      = 0xFF

IPMI_CHANNEL_NUMBER_PRIMARY_IPMB                = 0x00
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_1   = 0x01
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_2   = 0x02
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_3   = 0x03
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_4   = 0x04
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_5   = 0x05
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_6   = 0x06
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_7   = 0x07
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_8   = 0x08
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_9   = 0x09
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_10  = 0x0A
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_SPECIFIC_11  = 0x0B
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_RESERVED_12  = 0x0C
IPMI_CHANNEL_NUMBER_IMPLEMENTATION_RESERVED_13  = 0x0D
IPMI_CHANNEL_NUMBER_PRIMARY_PRESENT_IF          = 0x0E
IPMI_CHANNEL_NUMBER_PRIMARY_SYSTEM_INTERFACE    = 0x0F
