#Read a Video Stream from Cmera(Frame by Frame)
import cv2

#Capturing the video from webcam where 0 which is the id of default webcam 
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

#ret is the return value if it is false then the inage is not captured properly
while True:
    ret,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
    if ret==False:
        continue
    #Here the second parameter is scaling ,it is required beacuse haarcascade_frontalface_alt has been train on some image of particular size
    #So scaling will try to reduce the sixe of ours  suppose here we have given 1,3 so it is reduce the image by 30% frame by frame
    #second parameter is number of neighbours
    faces=face_cascade.detectMultiScale(gray_frame,1.3,5)
    
    #This above function will return the x,y corrdinates as well as width and height of face inage
    
    
    
    #THIS BELOW FUNCTION WILL CREATE A RECTANGLE ON THE FACE WHERE X+W AND Y+H ARE COORDINATES ON OPPOSITE END SIDE
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    
    
    cv2.imshow("Video Frame",frame)

    
    key_pressed=cv2.waitKey(1) & 0xFF  #0xFF is 8  one's  so here we are converting 32 bit number to 8 bit number
    if key_pressed==ord('q'):  #Once pressed q it will close
        break


cap.release()
cv2.destroyAllWindows()