from numpy import byte, uint16
import sys
from ClientFiles_Python import Client_API, ReturnCodes

def startCam():
    cam = Client_API.Initialize("COM3")
    maxChunkSize = uint16(256)
    captureIndex = byte(0)
    capSettings = Client_API.FLR_CAPTURE_SETTINGS_T
    capSettings.dataSrc = Client_API.FLR_CAPTURE_SRC_E.FLR_CAPTURE_SRC_TNF
    capSettings.numFrames = 1
    capSettings.bufferIndex = captureIndex

    img = Client_API.captureFrames(capSettings)
    #print(img)
    frame = Client_API.memReadCapture(capSettings.bufferIndex,)
    a = Client_API.memGetCaptureSize()
    b = Client_API.memGetFlashSize()
    c = Client_API.memEraseFlash()
    d = Client_API.memWriteFlash()
    e = Client_API.memReadFlash()

    print(frame)
startCam()
    
            


# serial = Client_API.bosonGetCameraSN()

# print(serial)
