import numpy as np
import cv2

line_thickness = 1
circle_radius = 20


def onMouse(event, x, y, flags, params):
    global title, image, line_thickness, circle_radius
    pt = (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, pt, circle_radius, (0, 0, 255), line_thickness)  # image, point, radius, color, thickness
        cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, pt, (x + 30, y + 30), (100, 100, 100), line_thickness)  # image, pt1, pt2, color, thickness
        cv2.imshow(title, image)


def onLineThicknessTrackbarChange(value):
    global line_thickness
    line_thickness = value


def onCircleRadiusTrackbarChange(value):
    global circle_radius
    circle_radius = value


image = np.ones((300, 300, 3), np.uint8) * 255
title = "window"

cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)

cv2.createTrackbar('thickness', title, line_thickness, 10, onLineThicknessTrackbarChange)
cv2.createTrackbar('radius', title, circle_radius, 50, onCircleRadiusTrackbarChange)

cv2.waitKey(0)
cv2.destroyAllWindows()
