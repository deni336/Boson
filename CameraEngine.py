from flirpy.camera.boson import Boson
from flirpy.util.raw import raw2temp
import cv2, threading
from tkinter import BitmapImage
from FrontEnd import BosonFront


metaDictionary = {"Atmospheric Trans Alpha 1" : 0.006569, "Atmospheric Trans Alpha 2" : 0.012620,
                "Atmospheric Trans Beta 1" : -0.002276, "Atmospheric Trans Beta 2" : -0.00667,
                "Atmospheric Trans X" : 1.900000, "Planck R1" : 21106.77,
                "Planck R2" : 0.012545258, "Planck O" : -7340.0,
                "Planck B" : 1501.0, "Planck F" : 1.0,
                "Emissivity" : 1.0, "IR Window Transmission" : 1.0,
                "IR Window Temperature" : 20.0,"Object Distance" : 1.0,
                "Atmospheric Temperature" : 20.0, "Reflected Apparent Temperature" : 20.0,
                "Relative Humidity" : 50.0}
        
class CameraThermalData():
    def __init__(self) -> None:
        pass
    def callThermalData():
        conn = CameraConnection.connect()
        perFrameTemp = conn.grab()
        for temp in perFrameTemp:
            convertedFpaTemp = raw2temp(temp, metaDictionary)
            #print(convertedFpaTemp)
            return convertedFpaTemp

class CameraStream():
    def __init__(self) -> None:
        BosonFront.startBitmapOverlay()
    def videoStream():
        conn = cv2.VideoCapture(0)
        _, frame = conn.read()
        #frames = cv2.applyColorMap(frame, colormap=cv2.COLORMAP_COOL)
        cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2ImageResize = cv2.resize(cv2Image, (1800, 1005))
        return cv2ImageResize
        


class CameraConnection():
    def __init__(self) -> None:
        pass
    def connect():
        try:
            portNumber = Boson.find_serial_device()
        except:
            portNumber = Boson.find_video_device()
        conn = Boson(portNumber)
        return conn

