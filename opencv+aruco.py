





#load the image
image= cv2.imread("")

#resize the image
image = imutils.resize(image, width=500)

#convert the image to grayscale and remove gaussian blur
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(7,7),0)

#perform edge detection by first dilating and then erosion 
#to join broken boundaries of objectb edges
edged=cv2.Canny(gray,50,100)
edged = cv2.dilate(edged, None, iterations=1)
edged= cv2.erode(edged, None, iterations=1)

#find contours in the edge map
cnts=cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)

#sort the contours from left-to-right
(cnts,_)= contours.sort_contours(cnts)

def findArucoMarkers(img,markerSize=a , totalMarkers=b , draw=True):
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(cv2.aruco, f'DICT_{markerSize})