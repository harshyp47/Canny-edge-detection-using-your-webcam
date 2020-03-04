import cv2
import numpy as np


cap = cv2.VideoCapture(0)
t=14
while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    #laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    L2 = cv2.Canny(blurred_frame, 1*t, 6*t,L2gradient=True)
    cv2.imshow("Frame", frame)
    #cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Canny", L2)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()