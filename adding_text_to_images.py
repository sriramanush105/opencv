#importing required packages
import cv2
import numpy
#reading image using cv2 imread method
image_1=cv2.imread(r"C:\Users\Sriram\Desktop/efil.jpg")
#declaring text to be added
text="hello this is gonna be crazy.."
#declaring position from which text line should start
org=(20,image_1.shape[0]-20)
#declaring font type of text
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
#declaring color
color=(255,255,255)#bgr value for white
# declaring font scale value
fontscale=1.1
#declaring thickness of line
thickness=1
## now adding text to image using cv2 putText method with above parameters
image_texted=cv2.putText(image_1,text,org,font,fontscale,color,thickness,cv2.LINE_AA)
## displayiing texted image with cv2 imshow method
cv2.imshow("texted image",image_texted)
#saving the texted image using cv2 imwrite method
cv2.imwrite(r"C:\Users\Sriram\Desktop/image_texted.jpg",image_texted)
