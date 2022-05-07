from ast import Index
import threading, serial, io
from cv2 import exp
import numpy as np
from numpy import frombuffer, number
from ClientFiles_Python import Client_API, EnumTypes
from ClientFiles_Python.ReturnCodes import FLR_RESULT
from tkinter import *
from tkinter import BitmapImage, ttk
import PIL
from PIL import ImageTk, Image
import cv2, re
import GUI as G



class BosonFront(G.GUI):

    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        topLabel = ttk.Label(self.mainFrame, text="Boson Viewer", font=["Arial", 24, "bold"], 
                            background="#4b4b4b", foreground="blue")
        topLabel.pack(side="top", anchor="n")

        utilFrame = LabelFrame(self.mainFrame, G.frameStyles, text="Utilities")
        utilFrame.pack(side='left', fill="y", expand=1, anchor="w")

        # Loop for creating buttons
        btnGroup = ["snapShot", "startScreenRecord", "stopScreenRecord", "forceFFC", "tankLevel", "delta", "rate"]
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

        
        # videoThread = threading.Thread(target=CameraAcquisition.acquireCamera(self))
        # videoThread.start()
    
    def delta():
        pass

    def rate():
        pass

    def startScreenRecord():
        pass

    def stopScreenRecord():
        pass

    def snapShot(*args):
        snapBool = False
        if args == True:
            snapBool = True
        elif args == False:
            snapBool = False
        return snapBool
    
    def forceFFC():
        pass


class CameraAcquisition(G.GUI):
    def __init__(self, parent) -> None:
        pass
        
    def acquireCamera(self):
        cameraFrame = Frame(self.mainFrame, bg= "#4b4b4b").pack()
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
            rawLst1 = []
            rawLstF = []
            offset = 0
            for offset in range(0, int(chunks)):
                if offset < memCapReturn[1]:
                    offset+=MAX_CHUNK_SIZE
                if memCapReturn[1]-offset > MAX_CHUNK_SIZE:
                    sizeInBytes = MAX_CHUNK_SIZE
                else:
                    sizeInBytes = memCapReturn[1] - offset

                memReadReturn = Client_API.memReadCapture(captureIndex, offset, sizeInBytes)
                
                rawLst.append(memReadReturn[1])
            thermLst = []
            for i in rawLst:
                for o in i:
                    if i.index(o) % 2:
                        thermLst.append(o)
                    elif len(rawLst1) != 640:
                        rawLst1.append(o)
                    elif len(rawLst1) == 640:
                        rawLstF.append(rawLst1)
                        rawLst1.clear()
                        rawLst1.append(o)
                    else:
                        rawLstF.append(rawLst1)
                        rawLst1.clear()
            #print(rawLstF)
            array = np.asarray(rawLst, dtype=np.uint8)
            newImage = Image.fromarray(array)
            
            displayBmap = BitmapImage(data=newImage)
            cameraLabel = Label(cameraFrame,image=displayBmap).pack()

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
