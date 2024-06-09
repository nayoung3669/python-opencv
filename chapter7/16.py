import cv2, numpy as np


def morphology(img, mask=None, mode=0):  # mode로 erode, dilate 합치기
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    mcnt = cv2.countNonZero(mask)  # 5개 영역
    for i in range(ycenter, img.shape[0] - ycenter):  # 1차원 배열
        for j in range(xcenter, img.shape[1] - xcenter):  # 2차원 배열
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + ycenter + 1
            roi = img[y1:y2, x1:x2]  # 마스크 영역
            temp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(temp)  # and 연산의 결과 1인 갯수

            if mode == cv2.MORPH_ERODE:
                dst[i][j] = 255 if (cnt == mcnt) else 0  # 침식
            elif mode == cv2.MORPH_DILATE:
                dst[i, j] = 0 if (cnt == 0) else 255  # 팽창
