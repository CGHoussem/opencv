import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (48, 64, 432, 600)

__, frame = cap.read()
mask = np.zeros(frame.shape[:2], np.uint8)

cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

frame = frame*mask2[:,:,np.newaxis]

plt.imshow(frame)
plt.colorbar()
plt.show()

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()