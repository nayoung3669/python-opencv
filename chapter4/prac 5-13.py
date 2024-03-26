import cv2

image = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)

# JPEG 파일
cv2.imwrite("test.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 100])

# PNG 파일
cv2.imwrite("test.png", image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
