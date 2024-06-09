# 미디언 필터링 : 3 by 3 일 때 9개의 화솟값을 정렬한 후 가운데 값으로 출력

import cv2, numpy as np


def median_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2  # 마스크 절반 크기

    for i in range(center, rows - center):
        for j in range(center, cols - center):
            y1, y2 = i - center, i + center + 1  # 마스크 높이 범위
            x1, x2 = j - center, j + center + 1  # 마스크 너비 범위
            mask = image[y1:y2, x1:x2].flatten()  # 마스크 영역

            sort_mask = cv2.sort(mask, cv2.SORT_EVERY_COLUMN)  # 정렬
            dst[i, j] = sort_mask[sort_mask.size // 2].item()  # 중앙값을 출력 화소로 지정
    return dst


image = cv2.imread("./images/filter_avg.jpg")
if image is None: raise Exception("오류")

med_img1 = median_filter(image, 3)  # 3by3
cv2.imshow("image", med_img1)
cv2.waitKey(0)
