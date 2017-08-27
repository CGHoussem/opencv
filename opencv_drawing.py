import cv2
import numpy as np

img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)

cv2.line(img, (10, 10), (200, 200), (150, 0, 0), 5)
cv2.rectangle(img, (10, 10), (200, 200), (250, 150, 0), 10)
cv2.circle(img, (105, 105), 100, (0, 150, 250), -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 150), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV YAHOOOOO!", (0, 110), font, 1, (255, 255, 255), 1, cv2.LINE_AA)


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
