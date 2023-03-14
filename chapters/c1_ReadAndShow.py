import cv2
print("Package imported")
img=cv2.imread("Images/Jett.jpg")
cv2.imshow("OUTPUT",img)
# cv2.waitKey(1000) # 1 second 
cv2.waitKey(0)  # infinity