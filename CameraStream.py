import cv2, time
import BosonFront as BF
from pynput.keyboard import Key, Controller

from ClientFiles_Python import Client_API
from ClientFiles_Python.EnumTypes import FLR_COLORLUT_ID_E

global img

#palette = Client_API.colorLutSetId(FLR_COLORLUT_ID_E.FLR_COLORLUT_BLACKHOT)

def startStream():
    img = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    prevFrameTime = 0
    newFrameTime = 0
    while(img.isOpened()):
        ret, frame = img.read()
        if not ret:
            break
        gray = frame
        gray = cv2.resize(gray, (1920, 1080))
        newFrameTime = time.time()
        fps = 1/(newFrameTime-prevFrameTime)
        prevFrameTime = newFrameTime
        fps = int(fps)    
        fps = str(fps)
        cv2.putText(gray, fps, (1850, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)
        #imgCol = cv2.applyColorMap(gray, colormap=BF.BosonFront.setColorPalette())
        cv2.namedWindow("Viper", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Viper", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        #return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        cv2.imshow('Viper', gray)
        if cv2.waitKey(1) == 27:
            break
        # return imgCol
    img.release()
startStream()
def restartStream():
    keyboard = Controller()
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    startStream()

def stopStream():
    img.release()
    cv2.destroyAllWindows()
