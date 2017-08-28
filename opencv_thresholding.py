import cv2
import numpy as np


# Loading and showing the original image
img = cv2.imread("bookpage.jpg")
cv2.imshow("original", img)

# Convert the original image to grayscale
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculating the threshold
threshold = cv2.adaptiveThreshold(img2gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 53, 2)

# Showing thresholded image
cv2.imshow("threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
