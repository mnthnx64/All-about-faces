import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.Canny(frame, 0, 20)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 13: break

cv2.destroyAllWindows()