import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define the codec and create ViderWriter object
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter("test_output2.avi", fourcc, 20.0, (640, 480))

# Create 3 trackbars for threshold1, threshold2 and apertureSize
cv2.namedWindow("edges")
def nothing(x):
	pass
cv2.createTrackbar("Threshold 1", "edges", 100, 255, nothing)
cv2.createTrackbar("Threshold 2", "edges", 100, 255, nothing)
cv2.createTrackbar("apertureSize", "edges", 3, 10, nothing)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get trackbars values
    threshold1 = cv2.getTrackbarPos("Threshold 1", "edges")
    threshold2 = cv2.getTrackbarPos("Threshold 2", "edges")
    apertureSize = cv2.getTrackbarPos("apertureSize", "edges")

    # Detect the edges from the frame
    edges = cv2.Canny(gray, threshold1, threshold2, apertureSize)
    
    cv2.imshow("Webcam", frame)
    cv2.imshow("edges", edges)
    #out.write(gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
