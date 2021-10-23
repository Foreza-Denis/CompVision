import cv2
import numpy as np

img = np.zeros((400,500,3), np.uint8)
# img[:] = 255,255,255
# img[200:300, 100:200] = 0,0,0

cv2.line(img, (0,0), (250,0), (255,0,0), 5)
cv2.circle(img, (250,200), 50, (255,0,255), 10)
cv2.rectangle(img, (0,0), (250,200), (0,0,250), 5)
cv2.rectangle(img, (250,200), (500,400), (0,255,0), 5)
cv2.rectangle(img, (0,0), (250,200), (0,0,250), 5)
cv2.putText(img, "OOOOOOOOOOOHHHHHHHHHHHH", (0,200), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0,255,0))
cv2.imshow('image', img)
cv2.waitKey(0)