import numpy as np


def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]  # h, w


def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)  # 목적 영상 생성
    radian = (degree / 180) * np.pi  # 회전 각도 - 라디언
    sin, cos = np.sin(radian), np.cos(radian)  # 사인, 코사인 값 미리 계산

    for i in range(img.shape[0]):  # 목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x = j * cos + i * sin  # 회선 변환 수식
            if contain((y, x), img.shape):  # 입력 영상의 범위 확인
        # dst[i, j] = bilinear_value(img, [x, y])  # 화소값 양선형 보간
    return dst


def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # 100, 100으로 먼저 이동
