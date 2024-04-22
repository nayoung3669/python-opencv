import cv2, numpy as np

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

while True:  # 픽셀 읽기 무한반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break

    x, y, w, h = (200, 100, 200, 100)  # 200,100 좌표에서 200 * 100 tkdlwmfh gka
    cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)
    tmp = frame[y:y + h, w:w + x]  # y부터 h까지, w부터 x까지 -> 관심 영역의 프레임들만 추출

    # mean 함수 이용 방법
    average1 = tuple(map(int, cv2.mean(tmp)))

    # 행렬 순회 방식
    value = np.array([0, 0, 0], np.uint8)
    for row in tmp:
        for pixel in row:
            value += pixel
    average2 = (value / (w * h)).astype(int)
