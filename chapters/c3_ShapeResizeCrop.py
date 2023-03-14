import cv2
img=cv2.imread("Images/merc.jpg")
print(img.shape)
imgResize=cv2.resize(img,(1000,500)) #Width,Height
print(imgResize.shape)
imgCropped=img[0:200,200:500] #Height,width
cv2.imshow("Mercedes",img)
cv2.imshow("New IMG Mercedes",imgResize)
cv2.imshow("Cropped IMG Mercedes",imgCropped)
cv2.waitKey(0)
