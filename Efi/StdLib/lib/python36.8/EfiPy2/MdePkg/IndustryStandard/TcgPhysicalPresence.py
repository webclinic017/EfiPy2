# TcgPhysicalPresence.py
#
# EfiPy2.MdePkg.IndustryStandard.TcgPhysicalPresence
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
TCG_ACPI_FUNCTION_GET_PHYSICAL_PRESENCE_INTERFACE_VERSION      = 1
TCG_ACPI_FUNCTION_SUBMIT_REQUEST_TO_BIOS                       = 2
TCG_ACPI_FUNCTION_GET_PENDING_REQUEST_BY_OS                    = 3
TCG_ACPI_FUNCTION_GET_PLATFORM_ACTION_TO_TRANSITION_TO_BIOS    = 4
TCG_ACPI_FUNCTION_RETURN_REQUEST_RESPONSE_TO_OS                = 5
TCG_ACPI_FUNCTION_SUBMIT_PREFERRED_USER_LANGUAGE               = 6
TCG_ACPI_FUNCTION_SUBMIT_REQUEST_TO_BIOS_2                     = 7
TCG_ACPI_FUNCTION_GET_USER_CONFIRMATION_STATUS_FOR_REQUEST     = 8

TCG_PP_OPERATION_RESPONSE_SUCCESS              = 0x0
TCG_PP_OPERATION_RESPONSE_USER_ABORT           = 0xFFFFFFF0
TCG_PP_OPERATION_RESPONSE_BIOS_FAILURE         = 0xFFFFFFF1

TCG_PP_RETURN_TPM_OPERATION_RESPONSE_SUCCESS                   = 0
TCG_PP_RETURN_TPM_OPERATION_RESPONSE_FAILURE                   = 1

TCG_PP_SUBMIT_REQUEST_TO_PREOS_SUCCESS                                  = 0
TCG_PP_SUBMIT_REQUEST_TO_PREOS_NOT_IMPLEMENTED                          = 1
TCG_PP_SUBMIT_REQUEST_TO_PREOS_GENERAL_FAILURE                          = 2
TCG_PP_SUBMIT_REQUEST_TO_PREOS_BLOCKED_BY_BIOS_SETTINGS                 = 3

TCG_PP_GET_USER_CONFIRMATION_NOT_IMPLEMENTED                                 = 0
TCG_PP_GET_USER_CONFIRMATION_BIOS_ONLY                                       = 1
TCG_PP_GET_USER_CONFIRMATION_BLOCKED_BY_BIOS_CONFIGURATION                   = 2
TCG_PP_GET_USER_CONFIRMATION_ALLOWED_AND_PPUSER_REQUIRED                     = 3
TCG_PP_GET_USER_CONFIRMATION_ALLOWED_AND_PPUSER_NOT_REQUIRED                 = 4

TCG_PHYSICAL_PRESENCE_NO_ACTION                               = 0
TCG_PHYSICAL_PRESENCE_ENABLE                                  = 1
TCG_PHYSICAL_PRESENCE_DISABLE                                 = 2
TCG_PHYSICAL_PRESENCE_ACTIVATE                                = 3
TCG_PHYSICAL_PRESENCE_DEACTIVATE                              = 4
TCG_PHYSICAL_PRESENCE_CLEAR                                   = 5
TCG_PHYSICAL_PRESENCE_ENABLE_ACTIVATE                         = 6
TCG_PHYSICAL_PRESENCE_DEACTIVATE_DISABLE                      = 7
TCG_PHYSICAL_PRESENCE_SET_OWNER_INSTALL_TRUE                  = 8
TCG_PHYSICAL_PRESENCE_SET_OWNER_INSTALL_FALSE                 = 9
TCG_PHYSICAL_PRESENCE_ENABLE_ACTIVATE_OWNER_TRUE              = 10
TCG_PHYSICAL_PRESENCE_DEACTIVATE_DISABLE_OWNER_FALSE          = 11
TCG_PHYSICAL_PRESENCE_DEFERRED_PP_UNOWNERED_FIELD_UPGRADE     = 12
TCG_PHYSICAL_PRESENCE_SET_OPERATOR_AUTH                       = 13
TCG_PHYSICAL_PRESENCE_CLEAR_ENABLE_ACTIVATE                   = 14
TCG_PHYSICAL_PRESENCE_SET_NO_PPI_PROVISION_FALSE              = 15
TCG_PHYSICAL_PRESENCE_SET_NO_PPI_PROVISION_TRUE               = 16
TCG_PHYSICAL_PRESENCE_SET_NO_PPI_CLEAR_FALSE                  = 17
TCG_PHYSICAL_PRESENCE_SET_NO_PPI_CLEAR_TRUE                   = 18
TCG_PHYSICAL_PRESENCE_SET_NO_PPI_MAINTENANCE_FALSE            = 19
TCG_PHYSICAL_PRESENCE_SET_NO_PPI_MAINTENANCE_TRUE             = 20
TCG_PHYSICAL_PRESENCE_ENABLE_ACTIVATE_CLEAR                   = 21
TCG_PHYSICAL_PRESENCE_ENABLE_ACTIVATE_CLEAR_ENABLE_ACTIVATE   = 22

TCG_PHYSICAL_PRESENCE_VENDOR_SPECIFIC_OPERATION               = 128

TCG2_PHYSICAL_PRESENCE_NO_ACTION                                         = 0
TCG2_PHYSICAL_PRESENCE_ENABLE                                            = 1
TCG2_PHYSICAL_PRESENCE_DISABLE                                           = 2
TCG2_PHYSICAL_PRESENCE_CLEAR                                             = 5
TCG2_PHYSICAL_PRESENCE_ENABLE_CLEAR                                      = 14
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_CLEAR_TRUE                    = 17
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_CLEAR_FALSE                   = 18
TCG2_PHYSICAL_PRESENCE_ENABLE_CLEAR_2                                    = 21
TCG2_PHYSICAL_PRESENCE_ENABLE_CLEAR_3                                    = 22
TCG2_PHYSICAL_PRESENCE_SET_PCR_BANKS                                     = 23
TCG2_PHYSICAL_PRESENCE_CHANGE_EPS                                        = 24
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_CHANGE_PCRS_FALSE             = 25
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_CHANGE_PCRS_TRUE              = 26
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_TURN_ON_FALSE                 = 27
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_TURN_ON_TRUE                  = 28
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_TURN_OFF_FALSE                = 29
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_TURN_OFF_TRUE                 = 30
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_CHANGE_EPS_FALSE              = 31
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_CHANGE_EPS_TRUE               = 32
TCG2_PHYSICAL_PRESENCE_LOG_ALL_DIGESTS                                   = 33
TCG2_PHYSICAL_PRESENCE_DISABLE_ENDORSEMENT_ENABLE_STORAGE_HIERARCHY      = 34
TCG2_PHYSICAL_PRESENCE_NO_ACTION_MAX                                     = 34

TCG2_PHYSICAL_PRESENCE_STORAGE_MANAGEMENT_BEGIN                          = 96
TCG2_PHYSICAL_PRESENCE_ENABLE_BLOCK_SID                                  = 96
TCG2_PHYSICAL_PRESENCE_DISABLE_BLOCK_SID                                 = 97
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_ENABLE_BLOCK_SID_FUNC_TRUE    = 98
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_ENABLE_BLOCK_SID_FUNC_FALSE   = 99
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_DISABLE_BLOCK_SID_FUNC_TRUE   = 100
TCG2_PHYSICAL_PRESENCE_SET_PP_REQUIRED_FOR_DISABLE_BLOCK_SID_FUNC_FALSE  = 101

TCG2_PHYSICAL_PRESENCE_VENDOR_SPECIFIC_OPERATION                         = 128

