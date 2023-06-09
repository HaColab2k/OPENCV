import requests
import cv2
import numpy as np
import imutils
  
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.21.124:8080/shot.jpg"

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>300:
            cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h=cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,ColorPurple):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,ColorPurple,cv2.FILLED)
"""----------------------------------------------------------"""
Color=(179,10,162)
myPoints=[]# [x,y,colorId]  
# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=700, height=400)
    img=cv2.flip(img, 1)
    imgResult=img.copy()
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    newPoints=[]
    lower=np.array([0,84,227] ) #0 171 84 162 227 255
    upper=np.array([171,162,255])
    mask = cv2.inRange(imgHSV,lower,upper)
    x,y=getContours(mask)
    cv2.circle(imgResult,(x,y),10,Color,cv2.FILLED)
    if x!=0 and y!=0:
        newPoints.append([x,y])
    # imgResult=cv2.bitwise_and(img,img,mask=mask)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,Color)
    imgStack=stackImages(0.7,[img,mask,imgResult])
    cv2.imshow("stack images",imgStack)
  
    # Press Esc key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'): # press q to quite
        break
  
cv2.destroyAllWindows()