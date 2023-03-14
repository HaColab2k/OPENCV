import cv2
cap=cv2.VideoCapture(0) # 0 for default webcam
print("Press q to quite")
# Set size
cap.set(3,680) # ID: 3 . width
cap.set(4,480) # ID: 4 , height
# Set brightness 
cap.set(10,10) # ID 10: brightness
while True:
    # success is boolean value
    success, img = cap.read()
    cv2.imshow("My Webcam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
