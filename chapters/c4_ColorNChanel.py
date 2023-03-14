import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8) # create a 512x512 Black IMG => "3),np.uint8" to color
print(img.shape)
img[0:250,0:50]=255,0,0 # change to blue from height 0 to 255 and width 0 to 50, BGR order
cv2.imshow("Image",img)
cv2.waitKey(0)