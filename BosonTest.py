from numpy import byte, size, ubyte, uint16, uint32
from ClientFiles_Python import Client_API, EnumTypes
from ClientFiles_Python.ReturnCodes import FLR_RESULT
from FSLP_Files import UART_HalfDuplex

MAX_CHUNK_SIZE = 256

cam = Client_API.Initialize("COM3")
captureIndex = 0
capSettings = Client_API.FLR_CAPTURE_FILE_SETTINGS_T
capSettings.dataSrc = Client_API.FLR_CAPTURE_SRC_E.FLR_CAPTURE_SRC_TNF
capSettings.numFrames = 1
capSettings.bufferIndex = captureIndex

returnCode = Client_API.captureFrames(capSettings)
if returnCode != FLR_RESULT.R_SUCCESS:
    cam.close()
# print(returnCode)

errorCount = 0

memCapReturn = Client_API.memGetCaptureSize()
frameSize = memCapReturn[1]
rows = memCapReturn[2]
columns = memCapReturn[3]
# print(memCapReturn)
chunks = (frameSize/MAX_CHUNK_SIZE)+0.5
offset=0
n = (offset<frameSize)
m = (offset + MAX_CHUNK_SIZE)

for n in range(0, m):
    if frameSize-offset > MAX_CHUNK_SIZE:
        sizeInBytes = MAX_CHUNK_SIZE
    else:
        sizeInBytes = frameSize - offset

    memReadReturn = Client_API.memReadCapture(captureIndex, offset, sizeInBytes)
# print(memReadReturn)
captureIndex = 1

returnCode = Client_API.captureFrames(capSettings)

memCapReturn = Client_API.memGetCaptureSize()
frameSize = memCapReturn[1]
rows = memCapReturn[2]
columns = memCapReturn[3]
# print(memCapReturn)

chunks = (frameSize / MAX_CHUNK_SIZE) + 0.5
offset = 0
n = offset < chunks

for n in range(offset+1):
    if frameSize - offset * MAX_CHUNK_SIZE > MAX_CHUNK_SIZE:
        sizeInBytes = MAX_CHUNK_SIZE
    else:
        sizeInBytes = frameSize - offset * MAX_CHUNK_SIZE
    memCapReturn = Client_API.memReadCapture(captureIndex, offset, sizeInBytes)

locationEnum = EnumTypes.FLR_MEM_LOCATION_E.FLR_MEM_LENS_GAIN
locationIdx = 1
memFlashReturn = Client_API.memGetFlashSize(locationEnum)

# print(memFlashReturn)

inputD = ''
count = 0
while count < memFlashReturn[1]:
    inputD = inputD + '0x00,'
    inputD = inputD + '0x20,'
    count+=2
    
inputData = bytearray(inputD, 'utf-8')


chunks = (memFlashReturn[1] / MAX_CHUNK_SIZE) + 0.5
data = []
datas = []
for idx in range(int(chunks)):
    
    if (frameSize - idx * MAX_CHUNK_SIZE) > MAX_CHUNK_SIZE:
        sizeInBytes = MAX_CHUNK_SIZE
    else:
        sizeInBytes = (frameSize - idx * MAX_CHUNK_SIZE)
    datas.clear()
    for idx2 in range(sizeInBytes):
        datas.insert(idx2, inputData[(idx * MAX_CHUNK_SIZE + idx2)])
    data.append(datas)
        
# print(data)

memEraseFlashReturn = Client_API.memEraseFlash(locationEnum, locationIdx)

for chunkIdx in range(int(chunks+1)):
    offset = (chunkIdx * MAX_CHUNK_SIZE)
    if ((memFlashReturn[1] - offset) > MAX_CHUNK_SIZE):
        sizeInBytes = MAX_CHUNK_SIZE
    else:
        sizeInBytes = (memFlashReturn[1] - offset)
    memWriteFlashReturn = Client_API.memWriteFlash(locationEnum,locationIdx, offset, sizeInBytes, data[chunkIdx])

    for chunk_idx in range(int(chunks+1)):
        offset = (chunk_idx * MAX_CHUNK_SIZE)
        if (memFlashReturn[1] - offset) > MAX_CHUNK_SIZE:
            sizeInBytes = MAX_CHUNK_SIZE
        else:
            sizeInBytes = (memFlashReturn[1] - offset)
        memReadFlashReturn = Client_API.memReadFlash(locationEnum, locationIdx, offset, sizeInBytes)
    print(memReadFlashReturn)