import cv2, time
import BosonFront as BF

class CameraStream:
    def __init__(self) -> None:
        pass

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
                    imgCol = cv2.applyColorMap(gray, colormap=BF.BosonFront.setColorPalette())
                    # cv2.namedWindow("Viper", cv2.WND_PROP_FULLSCREEN)
                    # cv2.setWindowProperty("Viper", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('Viper', imgCol)
                    if cv2.waitKey(1) == 27:
                        break
                    # return imgCol
                img.release()

                cv2.destroyAllWindows()