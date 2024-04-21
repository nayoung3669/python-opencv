import numpy as np
import cv2

image = np.full((300, 400), 100, np.uint8)
cv2.imshow("4-6", image)
resized_image = cv2.resize(image, (500, 600))
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
