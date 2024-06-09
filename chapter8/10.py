# 원본 영상을 (50,60) 좌표만큼 평행 이동을 수행하는 프로그램
# 어파인 변환의 워프 어파인 -> 회전, 크기변경, 평행이동 모두 수행 가능
# contain 함수로 이동했을 때 윈도우를 벗어나는지 확인

import numpy as np, cv2


def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]  # h, w


def translate(img, pt):  # 어느 point 만큼 이동할지
    dst = np.zeros(img.shape, img.dtype)  # 목적 영상, 순회
    for i in range(img.shape[0]):  # 역방향 사상
        for j in range(img.shape[1]):
            # 역방향 사상일 때 x = x' - dx , y = y' - dy
            x, y = np.subtract((j, i), pt)  # dx, dy가 pt
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

image = cv2.imread("images/translate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 읽기 에러")

tr_mat = np.array([[1,0,50], [0,1,60]], np.float32)

dst1 = translate(image, (50,60))
dst2 = cv2.warpAffine(image, tr_mat, image.shape[::-1], cv2.INTER_LINEAR)

