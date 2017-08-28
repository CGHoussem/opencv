import cv2
import numpy as np

def nothing(x):
	pass
cv2.namedWindow("output3")
cv2.createTrackbar("Weight 1", "output3", 5, 10, nothing)
cv2.createTrackbar("Weight 2", "output3", 5, 10, nothing)

img1 = cv2.imread("insect1.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("insect2.jpg", cv2.IMREAD_COLOR)

output = img1 + img2
output2 = cv2.add(img2, img1)

cv2.imshow("output1", output)
cv2.imshow("output2", output2)

while True:
	weight1 = cv2.getTrackbarPos("Weight 1", "output3")
	weight2 = cv2.getTrackbarPos("Weight 2", "output3")
	output3 = cv2.addWeighted(img1, weight1*.1, img2, weight2*.1, 0)

	cv2.imshow("output3", output3)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
