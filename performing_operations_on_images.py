##image resiezing
#importing packages required
import cv2
import numpy as np
#reading images using cv2 imread method
image_1=cv2.imread(r"c:\Users\Sriram/efil.jpg")
image_2=cv2.imread(r"c:\Users\Sriram/download1.jfif")
#resizing both images to (600,400) useing resize method
image_1=cv2.resize(image_1,(600,400))
image_2=cv2.resize(image_2,(600,400))
##performin addition and subtraction to images
##we need to remember that images are nothing but arrays in computer representation we can add subtract and multiply to get new intense images
image_3=image_1+image_2
##display image to see combined image
cv2.imshow("image3",image_3)
##addWeighted method to make particular percentage compositions from both images
image_4=cv2.addWeighted(image_1,0.7,image_2,0.3,0)
cv2.imshow("image4",image_4)
