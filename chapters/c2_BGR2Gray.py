import cv2 
import numpy as np

img=cv2.imread("Images/merc.jpg")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgBlur_k7=cv2.GaussianBlur(imgGray,(7,7),0) # kernel 7x7, sigma X =0
# imgBlur_k5=cv2.GaussianBlur(imgGray,(5,5),0)
# imgBlur_k3=cv2.GaussianBlur(imgGray,(3,3),0)

imgCanny=cv2.Canny(img,100,100) # 100 threshold
# imgCanny_k7=cv2.Canny(imgBlur_k7,100,100) 
# imgCanny_k5=cv2.Canny(imgBlur_k5,100,100)
# imgCanny_k3=cv2.Canny(imgBlur_k3,100,100)

kernel=np.ones((3,3),np.uint8)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)

imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray IMG",imgGray)

cv2.imshow("Blur IMG kernel 7",imgBlur_k7)
# cv2.imshow("Blur IMG kernel 5",imgBlur_k5)
# cv2.imshow("Blur IMG kernel 3",imgBlur_k3)

cv2.imshow("Canny edges detection",imgCanny)
# cv2.imshow("k7 Canny edges detection",imgCanny_k7)
# cv2.imshow("k5 Canny edges detection",imgCanny_k5)
# cv2.imshow("k3 Canny edges detection",imgCanny_k3)

cv2.imshow("Dialation image",imgDialation)

cv2.imshow("Eroded image",imgEroded)

cv2.waitKey(0)