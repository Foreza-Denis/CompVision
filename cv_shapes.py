import cv2
import numpy as np
import random as rnd

def getContours(img):
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgCont, contours, -1, (255,0), 2, cv2.LINE_8, hierarchy)
            pr = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*pr, True)
            x,y, w,h = cv2.boundingRect(approx)
            corner_count = len(approx)
            if corner_count == 3:
                object_type = 'Tri'
            elif corner_count == 4:
                side_ratio = w/float(h)
                if 0.98<side_ratio<1.03:
                    object_type = 'kvadrat'
                else:
                    object_type = 'chetyrehugolnik'
            elif corner_count == 8:
                object_type = 'krug'
            else:
                object_type = 'None'
            cv2.rectangle(imgCont, (x,y), (x+w, y+h), (0,255, 0))
            cv2.putText(imgCont, object_type, (x+w//2-10, y+h//2-10), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7, (0,0,0), 1)

def thresh_callback(val):
    imgCanny = cv2.Canny(imgBlur, val, val)
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    imgCont = np.zeros((imgCanny.shape[0], imgCanny.shape[1], 3), np.uint8)
    for i in range(len(contours)):
        color = (rnd.randint(0, 256), rnd.randint(0, 256), rnd.randint(0, 256))
        cv2.drawContours(imgCont, contours, i, color, 2, cv2.LINE_8, hierarchy)
    cv2.imshow('imgCont', imgCont)


img: np.ndarray = cv2.imread('shapes.png', cv2.IMREAD_COLOR)
imgCont = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 150, 150)
getContours(imgCanny)
#Создаём окно
#source_wind = 'source'
#cv2.namedWindow(source_wind)
#cv2.imshow(source_wind, img)
#max_thresh = 500
#thresh = 100
#trackbar = cv2.createTrackbar("Canny:", source_wind, thresh, max_thresh, thresh_callback)


cv2.imshow('Korova', imgCont)
cv2.waitKey(0)