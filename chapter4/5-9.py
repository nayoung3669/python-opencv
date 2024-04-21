import numpy as np
import cv2

image = np.full((600, 400, 3), (255, 255, 255), np.uint8)
# 빨간색 사각형 그리기
cv2.rectangle(image, (100, 100), (200, 300), (0, 0, 255), 2)

cv2.imshow("window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
