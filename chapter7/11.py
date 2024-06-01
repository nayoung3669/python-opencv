import cv2
from Common.filters import diffrential

image = cv2.imread("./images/edge.jpg")
if image is None: raise Exception("오류")

# 로버츠 마스크
data1 = [[-1, 0, 0],
         [0, 1, 0],
         [0, 0, 0]]
data2 = [[0, 0, -1],
         [0, 1, 0],
         [0, 0, 0]]

# 프리윗 마스크
data3 = [-1, 0, 1,
         -1, 0, 1,
         -1, 0, 1]
data4 = [-1, -1, -1,
         0, 0, 0,
         1, 1, 1]

# 소벨 마스크 (프리윗이랑 비슷한데 가운데꺼가 2 또는 -2)
data5 = [-1, 0, 1,
         -2, 0, 2,
         -1, 0, 1]
data6 = [-1, -2, -1,
         0, 0, 0,
         1, 2, 1]

# diffrential 반환값 : 회선에서의 윤곽선의 크기, x축, y축
dst1, _, _ = diffrential(image, data1, data2)
dst2, _, _ = diffrential(image, data3, data4)
dst3, _, _ = diffrential(image, data5, data6)

cv2.imshow("roberts", dst1)
cv2.imshow("prewitt", dst2)
cv2.imshow("sobel", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
