import threading
from flirpy.camera.boson import Boson
from tkinter import *
from tkinter import BitmapImage, ttk
from PIL import ImageTk, Image
import cv2, re
import GUI as G
from CameraEngine import CameraThermalData



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
        
        cameraFrame = Frame(masterFrame, bg= "#4b4b4b").grid(row=0, column=1)
        lmain = Label(cameraFrame, bg= "#4b4b4b")
        lmain.grid(row=0, column=1)

        cap = cv2.VideoCapture(0)

        def videoStream():
            _, frame = cap.read()
            #frames = cv2.applyColorMap(frame, colormap=cv2.COLORMAP_COOL)
            #cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            #thermalData = CameraThermalData.callThermalData(frame)
            cv2ImageResize = cv2.resize(frame, (1680, 1005))
            img = Image.fromarray(cv2ImageResize)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(1, videoStream)
        videoThread = threading.Thread(target=videoStream())
        videoThread.start()
        # def videoStream1():
        #     try:
        #         portNumber = Boson.find_serial_device()
        #     except:
        #         portNumber = Boson.find_video_device()
        #     conn = Boson(portNumber)
        #     while conn != None:
        #         # Grabbing frame from Flirpy
        #         frame = conn.grab()
        #         #CameraThermalData.callThermalData(frame)
        # videoThread = threading.Thread(target=videoStream())
        # videoThread.start()
        
