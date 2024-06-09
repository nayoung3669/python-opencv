# 블러링 방법 3가지 : blur, boxFilter, GaussianBlur 방법
import cv2

image = cv2.imread("./images/filter_avg.jpg")
if image is None:
    raise Exception("오류")

# blur -> 5 by 5 mask면 모두 1/25로 블러링 됨
# borderType으로 마지막 값을 반복해서 씀
blur_img = cv2.blur(image, (5, 5), borderType=cv2.BORDER_CONSTANT)

# boxFilter
box_img = cv2.boxFilter(image, ddepth=-1, ksize=(5, 5))

# Gaussian Blur
gauss_img = cv2.GaussianBlur(image, (5, 5), 0)

# cv imshow
