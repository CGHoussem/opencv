import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 100)

    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)
    cv2.imshow("edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


"Exercice from opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html#exercises"
"""import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
	pass
cv2.namedWindow("edges")
cv2.createTrackbar("Threshold 1", "edges", 100, 500, nothing)
cv2.createTrackbar("Threshold 2", "edges", 100, 500, nothing)

while True:
	xThreshold = cv2.getTrackbarPos("Threshold 1", "edges")
	yThreshold = cv2.getTrackbarPos("Threshold 2", "edges")
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray, xThreshold, yThreshold)
	cv2.imshow("edges", edges)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()"""