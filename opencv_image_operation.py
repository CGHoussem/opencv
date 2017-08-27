import cv2
import numpy as np

img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

pancake = img[518:559, 179:255]

img[0:41, 0:76] = pancake


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
