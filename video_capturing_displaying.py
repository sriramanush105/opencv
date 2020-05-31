#import required packages
import numpy
import cv2
#creating videocapture() object which takes argument a file name or camera
capture=cv2.VideoCapture(0)
while (True):##craeting a infinte loop
    ##video capture object has read method that returns bool,image bool is status whether image can be read
    ret,frame=capture.read()
    ##we use cvtColor method to change captured frame to gray
    image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #displaying gray scaled image using imshow
    cv2.imshow("image",image)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
