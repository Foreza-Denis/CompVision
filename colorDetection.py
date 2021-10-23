import cv2
import numpy

img: numpy.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)

h, w, _ = img.shape
shrink_koeff = 2
img = cv2.resize(img, (w//shrink_koeff, h//shrink_koeff), cv2.INTER_NEAREST)

while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow("Orig", img)
    cv2.imshow("HSV", imgHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'): # в орд можно поставить 27, это esc
        break