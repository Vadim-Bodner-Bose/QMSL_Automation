import ctypes
from ctypes.wintypes import *
import os
from argparse import *
os.chdir('C:\\Program Files (x86)\\Qualcomm\\QDART\\bin')
lib = ctypes.CDLL('QMSL_MSVC10R')

#iWait_ms = ctypes.c_ulong(25)
iComPort = ctypes.c_uint(4)
#to double check that connection with com_port_auto returns the same result (handle) as the one with a known port
com_port_auto=ctypes.c_int(0xFFFF)
handle = lib.QLIB_ConnectServer(iComPort)
gResourceContext = HANDLE(handle)


channel = ctypes.c_int(5500)
phyID = ctypes.c_int(0)

#opcode = _OP_TX = 1
opCode = ctypes.create_string_buffer(b"1")
lib.QLIB_FTM_WLAN_TLV2_Create(gResourceContext, opCode)

lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, ctypes.byref(ctypes.create_string_buffer(b"channel")), ctypes.byref(ctypes.create_string_buffer(b"5500")))

lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, ctypes.byref(ctypes.create_string_buffer(b"txMode")), ctypes.byref(ctypes.create_string_buffer(b"0")))

lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, ctypes.byref(ctypes.create_string_buffer(b"phyId")), ctypes.byref(ctypes.create_string_buffer(b"0")))

lib.QLIB_FTM_WLAN_TLV2_Complete(gResourceContext)
