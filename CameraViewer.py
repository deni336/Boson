import cv2
import time

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
        imgCol = cv2.applyColorMap(gray, colormap=cv2.COLORMAP_AUTUMN)
        # cv2.namedWindow("Viper", cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty("Viper", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Viper', imgCol)
        if cv2.waitKey(1) == 27:
            break
        # return imgCol
    img.release()

    cv2.destroyAllWindows()
