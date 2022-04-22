from tracemalloc import Snapshot
from flirpy.camera.boson import Boson
from flirpy.util.raw import raw2temp
import numpy as np
import os, cv2, threading
from PIL import ImageTk, Image
from FrontEnd import BosonFront

# Dictionary for callThermalData to correct array to get temp.
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
    def callThermalData(frame):
        for temp in frame:
            convertedFpaTemp = raw2temp(temp, metaDictionary)
            #print(convertedFpaTemp)
            # Temp data conversion
            return convertedFpaTemp

class CameraOperations():
    def __init__(self) -> None:
        pass
    # Function for Flat Field Correction.
    def forceFFC():
        cam = Boson()
        returnCode = cam.do_ffc()
        if returnCode == None:
            print("FFC Complete")
        cam.release()

    def startScreenRecord():
        pass

    def stopScreenRecord():
        pass
    
    global currentFrame
    currentFrame = 0
    # Need to work snapshot in to make sure it works.
    def snapShot(*args):
        snapBool = False
        if args == True:
            snapBool = True
        elif args == False:
            snapBool = False
        return snapBool

class CameraStream():
    def __init__(self) -> None:
        pass
    
    def videoStream():
        try:
            portNumber = Boson.find_serial_device()
        except:
            portNumber = Boson.find_video_device()
        conn = Boson(portNumber)
        while conn != None:
            # Grabbing frame from Flirpy
            frame = conn.grab()
            #Changing color format to CV2 standard
            cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            # Resize to fit UI
            cv2ImageResize = cv2.resize(cv2Image, (1800, 1005))
            #img = Image.fromarray(cv2ImageResize)
            # converting type to cv2 standard
            cv2ImageResized = Image.fromarray((cv2ImageResize * 255).astype(np.uint8))
            #Pushing frame to Front end
            BosonFront.frameHandler(cv2ImageResized)
            #Giving frame to Thermal class
            # CameraThermalData.callThermalData(frame)
            # Start of camera loop
            if CameraOperations.snapShot() == True:
                try:
                    if not os.path.exists("C:/Users/denis/Pictures/SpiderMonkey"):
                        os.makedirs("C:/Users/denis/Pictures/SpiderMonkey")
                        name = './SpiderMonkey/frame' + str(currentFrame) + '.png'
                        print('Creating...', name)
                        # The above checks and/or creates file/folder. the lower is supposed to write the frame to the 
                        # file but it hasnt been creating the file. Possibly due to incorrect formatting.
                        cv2.imwrite(name, frame)
                        currentFrame += 1
                except OSError:
                    print('Error: Creating directory of data')
    videoStream()
        
        

        
        
        
        
