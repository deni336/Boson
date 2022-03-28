import cv2
deviceIndex = 0
cap = cv2.VideoCapture(deviceIndex+cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)

def startFrameCapture():
    framecount=600
    frameBuf=[]
    for _ in range(framecount): #record indefinitely (until user presses q), replace with "while True"
        streamRet, frame = cap.read()
        # if streamRet:
        #     cv2.imshow("image", frame)
        #     if cv2.waitKey(1) == ord('q'):
        #         break;
        frameBuf.append(frame)
    return frameBuf
            
    cv2.destroyAllWindows()

    #Below is example code to save images to "folder" (Use appropriate directory syntax.)
    num=0
    while len(frameBuf)>0:
        cv2.imwrite(f'{"C:/Users/denis/Documents/BosonScreenshots"}/cap_{num}.tiff', frameBuf.pop(0))
        num += 1