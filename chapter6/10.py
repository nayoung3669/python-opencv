import numpy as np
import cv2

# 영상 생성
image = np.zeros((50, 512), np.float32)  # 50 x 512 영상 생성

rows, cols = image.shape[:2]

for i in range(rows):  # 행렬 전체 조회
    for j in range(cols):
        image.itemset((i, j), 1 - (j / 512.0))  # 픽셀 값 설정, 0~1 범위로 조정

# 화면에 영상 출력
cv2.imshow("image", image)
cv2.waitKey(0)
