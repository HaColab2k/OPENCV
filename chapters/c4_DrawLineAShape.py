from pickletools import uint8
import cv2
import numpy as np

img=np.ones((512,512,3),np.uint8) # 3 chanel BGR , np.uint8 : 255 level
cv2.line(img,(0,0),(250,250),(0,255,0),5)  #(0,0): starting point,(250,250): ending point, (0,0,255): color chanel , 5 : thickness
cv2.rectangle(img,(50,50),(150,200),(0,0,255),3)
cv2.rectangle(img,(50,50),(150,150),(255,0,0),cv2.FILLED)
cv2.circle(img,(250,250),30,(150,150,150),4) #(250,250): center point, 30: radius
cv2.putText(img,"MCDD",(0,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,255,0),3) # 4: scale, 3 : thickness
cv2.imshow("IMG",img)
cv2.waitKey(0)