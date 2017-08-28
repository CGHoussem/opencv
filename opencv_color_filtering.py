import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread("background.jpg")

# cv2.namedWindow("custom")
# def nothing(x):
# 	pass
# cv2.createTrackbar("Blue1", "custom", 255, 255, nothing)
# cv2.createTrackbar("Green1", "custom", 255, 255, nothing)
# cv2.createTrackbar("Red1", "custom", 255, 255, nothing)
# cv2.createTrackbar("Blue2", "custom", 255, 255, nothing)
# cv2.createTrackbar("Green2", "custom", 255, 255, nothing)
# cv2.createTrackbar("Red2", "custom", 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # blue = cv2.getTrackbarPos("Blue1", "custom")
    # green = cv2.getTrackbarPos("Green1", "custom")
    # red = cv2.getTrackbarPos("Red1", "custom")
    # blue2 = cv2.getTrackbarPos("Blue2", "custom")
    # green2 = cv2.getTrackbarPos("Green2", "custom")
    # red2 = cv2.getTrackbarPos("Red2", "custom")

    # 75 0 35 - 122 255 255

    lower_blue = np.array([75, 0, 35])
    upper_blue = np.array([122, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_inv = cv2.bitwise_not(mask)

    #mask_inv = cv2.GaussianBlur(mask_inv, (5, 5), 0)
    #mask = cv2.GaussianBlur(mask, (5, 5), 0)

    mask_inv = cv2.medianBlur(mask_inv, 17)
    mask = cv2.medianBlur(mask, 17)

    bg = cv2.bitwise_and(img, img, mask=mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)

    res = cv2.add(bg, fg)

    cv2.imshow("res", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
