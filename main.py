import cv2
import numpy

img: numpy.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)

h, w, _ = img.shape
cv2.imshow('color', img)
img_resized = cv2.resize(img, (w//2, h//2), cv2.INTER_NEAREST)
print(img.shape)
cv2.imshow('resized', img_resized)

img_blur1 = cv2.blur(img, (3, 3))
img_blur2 = cv2.blur(img, (10, 10))
img_blur3 = cv2.blur(img, (30, 30))

cv2.imshow('img_blur', img_blur1)
cv2.imshow('img_blur', img_blur2)
cv2.imshow('img_blur', img_blur3)

b, g, r = cv2.split(img)
# cv2.imshow('blue', b)
# cv2.imshow('green', g)
# cv2.imshow('red', r)

merge_img = cv2.merge([b, g, r])
# cv2.imshow('merge_img', merge_img)

gray_img = cv2.imread('robot.jpeg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('gray_img',gray_img)

filled_img = img.copy()

for row in range(0, int(img.shape[0]/2)):
    for column in range(int(img.shape[1] / 2), img.shape[1]):
        filled_img[row, column]=[0, 0, 0]

# cv2.imshow('filled', img)
cropoed_img = img[100:250, 750:900]
#cv2.imshow('cropoed_img', cropoed_img)
cv2.waitKey()
