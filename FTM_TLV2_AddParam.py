
def addParam(gResourceContext, pKeyNullStr, pDataNullStr):
    #pass the pkeyNullStr and pDataNullStr as a byte object - Example: b'phyRFMode' for pKeyNullStr
    # b'0' for pDataNullStr
    #the pkeyNullStr MUST correspond the official pKey name used in QRCT4
    #make yourself familiar with debug scripts from the QRCT4 tool first.
    pKey = ctypes.create_string_buffer(pKeyNullStr)
    pData = ctypes.create_string_buffer(pDataNullStr)
    lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKey, pData)

