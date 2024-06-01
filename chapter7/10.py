# 평균 블러링은 가중치가 같음 (가우시안은 가운데꺼가 훨씬 많은 가중치)

import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("./images/filter_sharpen.jpg")
if image is None: raise Exception("오류")

# 샤프닝 마스크
mask1 = np.array([[-1, -1, -1],
                  [-1, 9, -1],
                  [-1, -1, -1]], np.float32)

# 블러링 마스크
mask2 = np.array([[1 / 9, 1 / 9, 1 / 9],
                  [1 / 9, 1 / 9, 1 / 9],
                  [1 / 9, 1 / 9, 1 / 9]], np.float32)

# 이미지 채널 분리
b, g, r = cv2.split(image)
# 각 채널에 대해 filter 적용
filtered1 = [filter(b, mask1), filter(g, mask1), filter(r, mask1)]  # 샤프닝 (user)
filtered2 = [filter(b, mask2), filter(g, mask2), filter(r, mask2)]  # 블러링 (user)

# 채널 병합
dst1 = cv2.merge(filtered1)
dst2 = cv2.filter2D(image, cv2.CV_8U, mask1)  # image, depth, kernel(mask)
dst3 = cv2.merge(filtered2)
dst4 = cv2.filter2D(image, cv2.CV_8U, mask2)  # 이미지에 mask2를 적용해라.

cv2.imshow("image", image)
cv2.imshow("sharpen user", cv2.convertScaleAbs((dst1)))  # 경곗값 줄이기
cv2.imshow("sharpen opencv", cv2.convertScaleAbs(dst2))
cv2.imshow("blurring user", cv2.convertScaleAbs(dst3))
cv2.imshow("blurring opencv", cv2.convertScaleAbs(dst4))
cv2.waitKey(0)
cv2.destroyAllWindows()
