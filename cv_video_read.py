#Read a Video Stream from Cmera(Frame by Frame)
import cv2

#Capturing the video from webcam where 0 which is the id of default webcam 
cap=cv2.VideoCapture(0)


#ret is the return value if it is false then the inage is not captured properly
while True:
    ret,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if ret==False:
        continue
    
    cv2.imshow("Video Frame",frame)
    cv2.imshow("Grame Frame",gray_frame)
    
    key_pressed=cv2.waitKey(1) & 0xFF  #0xFF is 8  one's  so here we are converting 32 bit number to 8 bit number
    if key_pressed==ord('q'):  #Once pressed q it will close
        break


cap.release()
cv2.destroyAllWindows()