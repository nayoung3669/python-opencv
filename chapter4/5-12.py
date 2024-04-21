import numpy as np
import cv2


def onChange(value):
    global image
    image = np.ones((300, 400), np.uint8) * value
    cv2.imshow(title, image)


image = np.zeros((300, 400), np.uint8)
title = "ex12"
bar_name = "Brightness"

cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.createTrackbar(bar_name, title, 0, 255, onChange)

while True:
    key = cv2.waitKeyEx(0)

    if key == 27:  # Esc 키
        break
    elif key == 63234:  # 왼쪽 화살표 키 (macOS 2020 Air)
        value = cv2.getTrackbarPos(bar_name, title)
        cv2.setTrackbarPos(bar_name, title, max(value - 10, 0))
    elif key == 63235:  # 오른쪽 화살표 키 (macOS 2020 Air)
        value = cv2.getTrackbarPos(bar_name, title)
        cv2.setTrackbarPos(bar_name, title, min(value + 10, 255))

cv2.destroyAllWindows()
