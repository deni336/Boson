# from numpy import byte, uint16
# import sys
# from ClientFiles_Python import Client_API, ReturnCodes

# def startCam():
#     cam = Client_API.Initialize("COM3")
#     maxChunkSize = uint16(256)
#     captureIndex = byte(0)
#     capSettings = Client_API.FLR_CAPTURE_SETTINGS_T
#     capSettings.dataSrc = Client_API.FLR_CAPTURE_SRC_E.FLR_CAPTURE_SRC_TNF
#     capSettings.numFrames = 1
#     capSettings.bufferIndex = captureIndex

#     img = Client_API.captureFrames(capSettings)
#     #print(img)
#     frame = Client_API.memReadCapture(capSettings.bufferIndex,)
#     a = Client_API.memGetCaptureSize()
#     b = Client_API.memGetFlashSize()
#     c = Client_API.memEraseFlash()
#     d = Client_API.memWriteFlash()
#     e = Client_API.memReadFlash()

#     print(frame)
# startCam()
from ClientFiles_Python import Client_API
from FSLP_Files.UART_HalfDuplex import PyUART

from flirpy.camera.boson import Boson
import serial

# cam = PyUART()
# port = cam.OpenPort("CameraSerialConfig.ini", "COM3", 921600)
# tele = cam.ReadFrame(5, 1)
# print(tele)



# ser = serial.Serial('COM3', 921600, timeout=0)
# setting = ser.get_settings()
# print(setting)
# while ser.is_open == True:
#     x = ser.readline(8)
#     print(x)
# while True:
#     data = ''
#     while ser.inWaiting()>0:
#         data += ser.read(1)
#     if data:
#         print ('Got:', data)
    
            


# # serial = Client_API.bosonGetCameraSN()

# # print(serial)

# from flirpy.camera.boson import Boson

# cap = Boson()

# returnCode = cap.get_nuc_desired()

# cap.do_nuc_table_switch()
# print(returnCode)


inp = '0x00' + ',' + '0x20'
inputData = bytearray(inp, 'utf-8')
print(inputData)


inp = bytes([0x00, 0x20, 0x00, 0x20])
print(inp)



mem = 655360
inp = []
count = 0
while count < mem:
    inp.append(0)
    inp.append(32)
    count+=2
inputData = bytearray(inp)
print(inputData, inp)
