import cv2

cap = cv2.VideoCapture(0, cv2.CAP_)
cap.set(cv2.CAP_PROP_FPS, 30)
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.resize(frame, (1920, 1080))
    imgCol = cv2.applyColorMap(gray, colormap=cv2.COLORMAP_TWILIGHT)
    cv2.namedWindow("Viper", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Viper", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Viper', imgCol)
    if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()