import cv2
import numpy as np

image=cv2.imread('images/input.jpg')

#store height and width of image
height, width =image.shape[:2]

quarter_height, quater_width=height/4, width/4

#T is our translation matrix
T=np.float32([[1,0,quarter_width],[0,1,quarter_width]])

#we use warpAffine to transform the image using matrix, T
img_translation =cv2.warpAffine(image, T,(width,height))
cv2.imshow('Translation,img_translation')
cv2.waitKey()
cv2.destroyAllWindows()

print(T)