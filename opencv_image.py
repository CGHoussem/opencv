import cv2
import numpy as np
import matplotlib.pyplot as plt
#								0
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHAGED = -1

"Showing the image with cv2"
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"Showing the image with pyplot"
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

"Saving the image with cv2"
cv2.imwrite("image_gray.png", img)


