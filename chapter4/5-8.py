import numpy as np
import cv2

mat1 = np.full((200, 300), 100, np.uint8)
mat2 = np.full((200, 300), 100, np.uint8)

h, w = mat1.shape  # mat2 의 시작위치
cv2.imshow("win 1", mat1)
cv2.imshow("win 2", mat2)

cv2.moveWindow("win 1", 0,0)
cv2.moveWindow("win 2", w , h)
cv2.waitKey(0)