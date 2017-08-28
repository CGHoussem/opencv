import cv2
import numpy as np

img1 = cv2.imread("insect2.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("image.jpg", cv2.IMREAD_COLOR)

# Convert image 1 to grayscale
img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Making ROI of image 2
rows, cols, channels = img1.shape
roi = img2[0:rows, 0:cols]

# Thresholding image 1 to create a mask
ret, mask = cv2.threshold(img1gray, 180, 255, cv2.THRESH_BINARY_INV)

# Inverted the mask
mask_inv = cv2.bitwise_not(mask)

# We masked the image 2 by the inverted mask
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# We masked the image 1 by the normal mask
img1_fg = cv2.bitwise_and(img1, img1, mask=mask)


# We added the images together (overlayed)
dst = cv2.add(img2_bg, img1_fg)

# We replaced the ROI in image 2 with the new overlayed images
img2[0:rows, 0:cols] = dst

cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
