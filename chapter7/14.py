# 이중 임계값을 트랙바로 만들기
import numpy as np, cv2
from Common.filters import filter


# 트랙바 콜백함수
def onTrackbar(value):
    th1 = cv2.getTrackbarPos('th1', 'canny edge')  # 낮은 임계값
    th2 = cv2.getTrackbarPos('th2', 'canny edge')  # 높은 임계값

    canny = cv2.Canny(image, th1, th2)
    cv2.imshow('canny edge', canny)


image = cv2.imread("./images/canny_test.jpg")
if image is None: raise Exception("오류")

cv2.createTrackbar('th1', 'canny edge', 50, 255, onTrackbar)
cv2.createTrackbar('th2', 'canny edge', 50, 255, onTrackbar)
onTrackbar(50)
cv2.waitKey(0)
