import cv2
import numpy

img: numpy.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)

h, w, _ = img.shape
shrink_koeff = 2
img = cv2.resize(img, (w//shrink_koeff, h//shrink_koeff), cv2.INTER_NEAREST)


cv2.imshow("Orig", img)
cv2.waitKey(0)