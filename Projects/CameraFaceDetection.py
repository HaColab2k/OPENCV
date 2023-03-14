import cv2
faceCascade=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0) # 0 for default webcam
# Set size
cap.set(3,680) # ID: 3 . width
cap.set(4,480) # ID: 4 , height
# Set brightness 
cap.set(10,200) # ID 10: brightness
while True:
    # success is boolean value
    success, img = cap.read()
    img=cv2.flip(img, 1) # 0, flip vertical, 1 flip horizontal
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(50,255,0),2)
        cv2.putText(img,"Human",(x+(w//2),y-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(50,255,0),2)
    cv2.imshow("My Webcam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #Press q to quite
        break
    