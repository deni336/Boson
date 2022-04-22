import tkinter as tk
from tkinter import *
import re
from tkinter import ttk, BitmapImage
from PIL import ImageTk, Image
import numpy as np
import os, threading
import cv2, sys
import GUI as G
from flirpy.camera.boson import Boson

# def startBitmapOverlay():
#         thermalTempOverlay = BitmapImage(CameraThermalData.callThermalData())
#         print(thermalTempOverlay)

colorMapDict = {"AUTUMN": cv2.COLORMAP_AUTUMN, "BONE": cv2.COLORMAP_BONE,
                "CIVIDIS": cv2.COLORMAP_CIVIDIS, "COOL": cv2.COLORMAP_COOL,
                "DEEPGREEN": cv2.COLORMAP_DEEPGREEN, "HOT": cv2.COLORMAP_HOT,
                "HSV": cv2.COLORMAP_HSV, "INFERNO": cv2.COLORMAP_INFERNO,
                "JET": cv2.COLORMAP_JET, "MAGMA": cv2.COLORMAP_MAGMA,
                "OCEAN": cv2.COLORMAP_OCEAN, "PARULA": cv2.COLORMAP_PARULA,
                "PINK": cv2.COLORMAP_PINK, "PLASMA": cv2.COLORMAP_PLASMA,
                "RAINBOW": cv2.COLORMAP_RAINBOW, "SPRING": cv2.COLORMAP_SPRING,
                "SUMMER": cv2.COLORMAP_SUMMER, "TURBO": cv2.COLORMAP_TURBO,
                "TWILIGHT": cv2.COLORMAP_TWILIGHT, "TWILIGHT SHIFTED": cv2.COLORMAP_TWILIGHT_SHIFTED,
                "VIRIDIS": cv2.COLORMAP_VIRIDIS, "WINTER": cv2.COLORMAP_WINTER}
currentColorPalette = 14
clicked = "INFERNO"

class BosonFront(G.GUI):

    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)
        global masterFrame
        masterFrame = Frame(self.mainFrame, bg= "#4b4b4b")
        masterFrame.grid()
        
        # utilFrame = LabelFrame(masterFrame, G.frameStyles, text="Utilities")
        # utilFrame.grid(row=0, column=0, sticky="nw")

        # tempDisplayFrame = LabelFrame(masterFrame, G.frameStyles, text="Temp")
        # tempDisplayFrame.grid(row=1, column=0)

        # btnGroup = ["snapShot", "startScreenRecord", "stopScreenRecord", "forceFFC"]
        # rowPlus = 2
        # for btn in btnGroup:
        #     btnCom = "CameraOperations." + btn + "()"
        #     textGroup = [s for s in re.split("([A-Z][^A-Z]*)", btn) if s]
        #     btnText = ''
        #     for text in textGroup:
        #         btnText += text.title() + " "
        #     btnText.strip()
        #     rowPlus += 1
        #     btn = ttk.Button(utilFrame, text=btnText, command=lambda: btnCom).grid(row=rowPlus, column=0, pady=2)
    
        def displayVideo(frame):
            cameraFrame = Frame(masterFrame, bg= "#4b4b4b").grid(row=0, column=1)
            lmain = Label(cameraFrame, bg= "#4b4b4b")
            lmain.grid(row=0, column=1, sticky="nw")    
            imgtk = ImageTk.PhotoImage(image=frame)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(1, displayVideo) 
        
        
        
        


        # clicked = StringVar()
        # clicked.set("")
        # drop = OptionMenu(utilFrame , clicked , *colorMapList)
        # drop.grid(row=0, column=0, pady=2, padx=5)
        # button = Button(utilFrame, text="Submit", command=lambda: showColorPaletteLabel()).grid(row=1, column=0, pady=2, padx=5)
        # label = Label(utilFrame, bg= "#4b4b4b", text="Palette")
        # label.grid(row=2, column=0, pady=2, padx=5) 
        # global currentColorPalette
        # currentColorPalette = clicked.get()

        # def showColorPaletteLabel():
        #     label.config(text=clicked.get())


    # def setColorPalette():
    #     colorMapNumber = colorMapDict.get(currentColorPalette)
    #     return colorMapNumber

       

    

