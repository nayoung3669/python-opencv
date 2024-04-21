import cv2

# 카메라 캡처 객체 생성
capture = cv2.VideoCapture(0)

fps = 15
delay = round(1000 / fps)
size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*"DIVX")  # 코덱
# 동영상 저장을 위한 VideoWriter 객체 생성
writer = cv2.VideoWriter('flip_test.avi', fourcc, 15, (640, 480))

while True:
    ret, frame = capture.read()  # 카메라로부터 프레임 읽기
    if not ret:
        break

    # 좌우로 뒤집기
    flipped_frame = cv2.flip(frame, 1)

    # 동영상 파일에 프레임 쓰기
    writer.write(flipped_frame)

    # 화면에 프레임 표시
    cv2.imshow('Flipped Frame', flipped_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시, 객체 해제 및 창 닫기
capture.release()
out.release()
cv2.destroyAllWindows()
