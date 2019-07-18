import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    (rectangles, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8))

    rectangles = np.array([[x, y, x+width, y+height] for(x, y, width, height) in rectangles])
    pick = non_max_suppression(rectangles, probs=None, overlapThresh=0.65)

    for(xA, yA, xB, yB) in pick:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
