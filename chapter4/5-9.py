import numpy as np
import cv2

image = 255 * np.ones((400, 600, 3), np.uint8)
# 빨간색 사각형 그리기
cv2.rectangle(image, (100, 100), (200, 300), (0, 0, 255), -1)

cv2.imshow("window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
