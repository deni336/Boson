import threading, serial
from flirpy.camera.boson import Boson
from flirpy.util.raw import raw2temp
from tkinter import *
from tkinter import BitmapImage, ttk
from PIL import ImageTk, Image
import cv2, re
import GUI as G

metaDictionary = {"Atmospheric Trans Alpha 1" : 0.006569, "Atmospheric Trans Alpha 2" : 0.012620,
                "Atmospheric Trans Beta 1" : -0.002276, "Atmospheric Trans Beta 2" : -0.00667,
                "Atmospheric Trans X" : 1.900000, "Planck R1" : 21106.77,
                "Planck R2" : 0.012545258, "Planck O" : -7340.0,
                "Planck B" : 1501.0, "Planck F" : 1.0,
                "Emissivity" : .995, "IR Window Transmission" : 1.0,
                "IR Window Temperature" : 20.0,"Object Distance" : 1.0,
                "Atmospheric Temperature" : 20.0, "Reflected Apparent Temperature" : 20.0,
                "Relative Humidity" : 50.0}

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

        def snapShot(*args):
            snapBool = False
            if args == True:
                snapBool = True
            elif args == False:
                snapBool = False
            return snapBool

        def callThermalData(frame):
            # cap = cv2.VideoCapture(2)
            # _, frame = cap.read()
            for temp in frame:
                convertedFpaTemp = raw2temp(temp, metaDictionary)
                print(convertedFpaTemp)
                # Temp data conversion
                return convertedFpaTemp


        # cap = cv2.VideoCapture(0)
        # # ser = serial.Serial('COM3', 921600, timeout = 0)
        # # ser.open()

        # def videoStream():
        #     _, frame = cap.read()
        #     # therm = ser.readline(16)
        #     # print(therm)
        #     #frames = cv2.applyColorMap(frame, colormap=cv2.COLORMAP_COOL)
        #     #cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        #     thermalData = callThermalData(frame)
        #     cv2ImageResize = cv2.resize(frame, (1680, 1005))
        #     img = Image.fromarray(cv2ImageResize)
        #     imgtk = ImageTk.PhotoImage(image=img)
        #     lmain.imgtk = imgtk
        #     lmain.configure(image=imgtk)
        #     lmain.after(1, videoStream)
        # videoThread = threading.Thread(target=videoStream())
        # videoThread.start()

        def videoStream1():
            try:
                portNumber = Boson.find_serial_device()
            except:
                portNumber = Boson.find_video_device()
            conn = Boson(portNumber)
            while conn != None:
                # Grabbing frame from Flirpy
                frame = conn.grab()
                callThermalData(frame)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)
                lmain.after(1, videoStream1)

        videoThread = threading.Thread(target=videoStream1())
        videoThread.start()
        
        
