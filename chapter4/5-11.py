import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global image, title, line_thickness, circle_radius
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 30, y + 30), (100, 100, 100), line_thickness)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), circle_radius, (100, 100, 100), line_thickness)
    cv2.imshow(title, image)


def onLineThicknessTrackbarChange(value):
    global line_thickness
    line_thickness = value


def onCircleRadiusTrackbarChange(value):
    global circle_radius
    circle_radius = value


image = np.ones((300, 300, 3), np.uint8) * 255
title = "window"

line_thickness = 1
circle_radius = 20

cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)

cv2.createTrackbar('선의 굵기', title, line_thickness, 10, onLineThicknessTrackbarChange)
cv2.createTrackbar('원의 반지름', title, circle_radius, 50, onCircleRadiusTrackbarChange)

cv2.waitKey(0)
cv2.destroyAllWindows()
