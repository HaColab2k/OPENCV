#warp to get the bird's eyes view
import numpy as np
import cv2
img=cv2.imread("Images/road.jpg")
width,height=150,300
pts1=np.float32([[289,144],[541,106],[9,441],[593,433]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Road",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)