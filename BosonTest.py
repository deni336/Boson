from ClientFiles_Python import Client_API

cam = Client_API.Initialize("COM3")
serial = Client_API.bosonGetCameraSN()
print(serial)
fpa = Client_API.roicGetFPATemp()
fpaTempTable = Client_API.roicGetFPATempTable()
#resetFactoryDefaults = Client_API.bosonRestoreFactoryDefaultsFromFlash()
boot = Client_API.bosonReboot()
frame = Client_API.captureFrames()
