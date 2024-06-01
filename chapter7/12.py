# 2차미분은 LoG, DoG (라플라시안 of 가우시안, Difference of 가우시안)
import cv2

image = cv2.imread("./images/dog.jpg")
if image is None: raise Exception("오류")

# 가우시안 블러링 (마스크 크기 9 by 9, sigmaX 가 0 이면 자동 계산)
gaus = cv2.GaussianBlur(image, (9, 9), 0, 0)

# DoG (가우시안들의 차 Difference)
gaus1 = cv2.GaussianBlur(image, (3, 3), 0)
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)
dst1 = gaus1 - gaus2

# LoG (가우시안 -> 후 라플라시안)
dst2 = cv2.Laplacian(gaus, cv2.CV_16S, 9)

# cv2 imshow들
