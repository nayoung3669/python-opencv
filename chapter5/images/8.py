import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8) # 마스크(image와 크기가 같은 검정 영상)
center = (190, 170) # 타원의 중심
# 타원 그리기
cv2.ellipse(mask, center, (50, 90), 0, 0, 360, (255, 255, 255), -1)
# image에 mask 씌우기
dst = cv2.add(image, image, mask=mask)

cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)