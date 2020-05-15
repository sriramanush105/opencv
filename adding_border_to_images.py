#importing required packages
import cv2
import numpy as np
#reading image using cv2 imread method
image_1=cv2.imread(r"C:\Users\Sriram\Desktop/efil.jpg")
#adding border to image using cv2 copyMakeBorder method
bordered_image=cv2.copyMakeBorder(image_1,20,20,20,20,cv2.BORDER_CONSTANT,None,(0,255,255))##here(0,255,255) resemble  color   of border in bgr
#displaying image using cv2 imshow method
cv2.imshow("bordered image",bordered_image)
##saving borderd image using cv2 imwrite method
cv2.imwrite(r"C:\Users\Sriram\Desktop/bordered.jpg",bordered_image)
