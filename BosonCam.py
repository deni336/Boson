import cv2

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.resize(frame, (1920, 1080))
    imgCol = cv2.applyColorMap(gray, colormap=cv2.COLORMAP_INFERNO)
    cv2.imshow('frame', imgCol)
    if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()