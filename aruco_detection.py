import cv2
from cv2 import aruco
import cv2.aruco as aruco
import numpy as np
import os


def findArucoMarker(img,markerSize= 6, totalMarkers=250,
      draw=True):
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'')
    arucoDict= aruco.Dictionary.get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected= aruco.detectMarkers(imgGray,
             arucoDict, parameters=arucoParam)
    print(ids)         

    if draw:
        aruco.drawDetectedMarker(img, bboxs)




def main():
    cap= cv2.VideoCapture(0)

    while True:
        success,img=cap.read()
        findArucoMarker(img)
        cv2.imshow("Image",img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()




