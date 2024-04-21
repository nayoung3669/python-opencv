import numpy as np
import cv2

#
# def onMouse(event, x, y, flags, param):
#     global title, pt  # 전역 변수 참조
#
#     if event == cv2.EVENT_RBUTTONDOWN or (
#             event == cv2.EVENT_LBUTTONDOWN and (flags & cv2.EVENT_FLAG_RBUTTON or flags & cv2.EVENT_FLAG_CTRLKEY)):
#         if pt[0] < 0:
#             pt = (x, y)  # 시작 좌표 지정
#         else:
#             major_axis = max(abs(x - pt[0]), abs(y - pt[1]))  # 장축 길이
#             minor_axis = min(abs(x - pt[0]), abs(y - pt[1]))  # 단축 길이
#             cv2.ellipse(image, pt, (major_axis, minor_axis), 0, 0, 360, (0, 255, 0), 2)
#             cv2.imshow(title, image)
#             pt = (-1, -1)  # 시작 좌표 초기화
#
#
# image = np.full((300, 500, 3), (255, 255, 255), np.uint8)  # 흰색 배경 영상
#
# pt = (-1, -1)  # 시작 좌표 초기화
# title = "Draw Event"
# cv2.imshow(title, image)  # 윈도우에 영상 띄우기
# cv2.setMouseCallback(title, onMouse)  # 마우스 콜백 함수 등록
# cv2.waitKey(0)

image = np.full((300, 700, 3), (255, 255, 255), np.uint8)
pt1, pt2 = (180, 150), (550, 150)  # 타원 center 좌표
size = (120, 60)  # 타원의 반지름 사이즈 (x,y)

# cv2.ellipse(img, center, radius, 타원의 각도, 호의 시작각도, 호의 종료각도, 선의 색상 , 선의 두께 ...)
# cv2.ellipse(image, pt1, size, 0, 0, 360, (255, 0, 0), 1)
# cv2.ellipse(image, pt1, size, 90, 0, 360, (255, 0, 0), 1)
cv2.ellipse(image, pt1, size, 0, 30, 270, (255, 0, 0), 1)
cv2.ellipse(image, pt1, size, 90, -45, 90, (255, 0, 0), 1)

cv2.imshow("Ellipse", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
