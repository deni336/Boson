import threading, serial, io
from numpy import frombuffer
import PIL
from ClientFiles_Python import Client_API, EnumTypes
from ClientFiles_Python.ReturnCodes import FLR_RESULT
from tkinter import *
from tkinter import BitmapImage, ttk
from PIL import *
from PIL import ImageTk, Image
from PIL.Image import *
from PIL.Image import Image
import cv2, re
import GUI as G



class BosonFront(G.GUI):

    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        masterFrame = Frame(self.mainFrame, bg= "#4b4b4b")
        masterFrame.grid()

        utilFrame = LabelFrame(masterFrame, G.frameStyles, text="Utilities")
        utilFrame.grid(row=0, column=0, sticky="nw")

        # Loop for creating buttons
        btnGroup = ["snapShot", "startScreenRecord", "stopScreenRecord", "forceFFC"]
        rowPlus = 2
        for btn in btnGroup:
            btnCom = "CameraOperations." + btn + "()"
            textGroup = [s for s in re.split("([A-Z][^A-Z]*)", btn) if s]
            btnText = ''
            for text in textGroup:
                btnText += text.title() + " "
            btnText.strip()
            rowPlus += 1
            btn = ttk.Button(utilFrame, text=btnText, command=lambda: btnCom).grid(row=rowPlus, column=0, pady=2)

        
        videoThread = threading.Thread(target=CameraAcquisition.acquireCamera(self))
        videoThread.start()
        

    def snapShot(*args):
        snapBool = False
        if args == True:
            snapBool = True
        elif args == False:
            snapBool = False
        return snapBool


class CameraAcquisition(G.GUI):
    def __init__(self, parent) -> None:
        cameraFrame = Frame(self.mainFrame, bg= "#4b4b4b").grid(row=0, column=1)
        
    def acquireCamera(self):
        MAX_CHUNK_SIZE = 256

        cam = Client_API.Initialize("COM3")
        captureIndex = 0
        capSettings = Client_API.FLR_CAPTURE_FILE_SETTINGS_T
        capSettings.dataSrc = Client_API.FLR_CAPTURE_SRC_E.FLR_CAPTURE_SRC_TNF
        capSettings.numFrames = 1
        capSettings.bufferIndex = captureIndex
        while cam != None:

            returnCode = Client_API.captureFrames(capSettings)
            if returnCode != FLR_RESULT.R_SUCCESS:
                cam.close()
            errorCount = 0
            memCapReturn = Client_API.memGetCaptureSize()

            chunks = (memCapReturn[1]/MAX_CHUNK_SIZE)+0.5
            rawLst = []
            offset = 0
            for offset in range(0, int(chunks)):
                if offset < memCapReturn[1]:
                    offset+=MAX_CHUNK_SIZE
                if memCapReturn[1]-offset > MAX_CHUNK_SIZE:
                    sizeInBytes = MAX_CHUNK_SIZE
                else:
                    sizeInBytes = memCapReturn[1] - offset

                memReadReturn = Client_API.memReadCapture(captureIndex, offset, sizeInBytes)
                
                
            tkPhotoImage = ImageTk.PhotoImage(tkImage)
            displayBmap = BitmapImage(data=rawLst)
            cameraLabel = Label(self.cameraFrame,image=displayBmap).pack()

            # captureIndex = 1

            # returnCode = Client_API.captureFrames(capSettings)

            # memCapReturn = Client_API.memGetCaptureSize()
            # frameSize = memCapReturn[1]
            # rows = memCapReturn[2]
            # columns = memCapReturn[3]

            # chunks = (frameSize / MAX_CHUNK_SIZE) + 0.5
            # offset = 0
            # n = offset < chunks
            # readCapFull1 = []
            # for n in range(offset+1):
            #     if frameSize - offset * MAX_CHUNK_SIZE > MAX_CHUNK_SIZE:
            #         sizeInBytes = MAX_CHUNK_SIZE
            #     else:
            #         sizeInBytes = frameSize - offset * MAX_CHUNK_SIZE
            #     memCapReturn = Client_API.memReadCapture(captureIndex, offset, sizeInBytes)
            #     readCapFull1.append(memCapReturn[1])
            # print(readCapFull1)
            # for byte in memReadReturn[1]:
                
            #     bArry2Img = io.BytesIO(bytes(byte))
            # displayBmap = BitmapImage(data=bArry2Img)
            # cameraLabel = Label(self.cameraFrame,image=displayBmap).pack()
