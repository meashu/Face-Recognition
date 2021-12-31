#Simple program to read and show an image

import cv2

img=cv2.imread('dog.png')
gray=cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Dog Image',img)
cv2.imshow('Dog\'s gray image',gray)

#waitkey(0)--  the program will stop when any key is pressed

cv2.waitKey(0)  #The windoiw will remain open for infinite time and if we put into any value that in will occur for particular time
cv2.destroyAllWindows()