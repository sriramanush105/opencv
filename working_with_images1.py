#importing required packages
import numpy as np
import cv2
#reading image from file path using cv2 imread method
image=cv2.imread(r"C:\Users\Sriram\Desktop/img.png")
#displaying image using cv2 imshow method
cv2.imshow("image",image)
#saving image in other name and extension using imwrite method
cv2.imwrite(r"C:\Users\Sriram\Desktop/saved_pic.jpg",image)
