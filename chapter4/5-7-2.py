import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global image, title
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(image, (x, y), 5, (100, 100, 100), 1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 30, y + 30), (100, 100, 100), 2)
    cv2.imshow(title, image)


image = np.ones((300, 300), np.uint8) * 255
title = "Draw Event"

cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
