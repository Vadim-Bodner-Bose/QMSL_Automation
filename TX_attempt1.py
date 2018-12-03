import ctypes
from ctypes.wintypes import *
import os
from argparse import *
os.chdir('C:\\Program Files (x86)\\Qualcomm\\QDART\\bin')
lib = ctypes.CDLL('QMSL_MSVC10R')
#print(lib._handle)
#handle = ctypes.c_int(lib._handle)
#delcare a char array
libVersion = ctypes.create_string_buffer(b"",25)
#pass a char array to a function by reference (via a pointer)
lib.QLIB_GetLibraryVersion(ctypes.byref(libVersion))
#dereference the pointer libVersion to read a value
# print(libVersion.value)

#QPST is the library mode = true
libMode = ctypes.c_uint8(1)
#libMode = ctypes.c_wchar_p('true')
#libMode = ctypes.create_string_buffer(b"true")
#libMode = ctypes.create_string_buffer(b"TRUE")
lib.QLIB_SetLibraryMode(libMode)
libMode.value

#APQ = 1
targetType = ctypes.c_uint8(1)
#targetType = ctypes.c_wchar_p(1)
#targetType = ctypes.create_string_buffer(b"1")
lib.QLIB_SetTargetType(targetType)

#iWait_ms = ctypes.c_ulong(25)
iComPort = ctypes.c_uint(4)
#to double check that connection with com_port_auto returns the same result (handle) as the one with a known port
com_port_auto=ctypes.c_int(0xFFFF)
handle = lib.QLIB_ConnectServer(iComPort)
gResourceContext = HANDLE(handle)

#Set the WLAN module type if not called assumes a wrong module
eModuletype = ctypes.c_uint32(1)
lib.QLIB_FTM_WLAN_SetModuleType(gResourceContext, eModuletype)

#try creating string_buffer and pass byref
#dllID = ctypes.c_wchar_p('qc6180')
dllID = ctypes.create_string_buffer(b"qc6180")
chipID = ctypes.c_uint(255)
#try creating string_buffer and pass byref
#bin_file = ctypes.c_wchar_p('C:\\Qualcomm\\WCN\\ProdTests\\refDesigns\\BoardData\\fakeBoardData_AR6180.bin')
bin_file = ctypes.create_string_buffer(b"C:\\Qualcomm\\WCN\\ProdTests\\refDesigns\\BoardData\\fakeBoardData_AR6180.bin")
iNVMem = ctypes.c_int(5)
# the call below should return 1 if returns zero, load is not successfull
#lib.QLIB_FTM_WLAN_Atheros_LoadDUT(handle, byref(dllID), byref(bin_file),iNVMem, chipID)
#lib.QLIB_FTM_WLAN_Atheros_LoadDUT(byref(handle), byref(dllID), byref(bin_file),iNVMem, chipID)
#lib.QLIB_FTM_WLAN_Atheros_LoadDUT(ctypes.byref(ctypes.c_uint(handle)), ctypes.byref(dllID), ctypes.byref(bin_file),iNVMem, chipID)
lib.QLIB_FTM_WLAN_Atheros_LoadDUT(gResourceContext, dllID, bin_file,iNVMem, chipID)









