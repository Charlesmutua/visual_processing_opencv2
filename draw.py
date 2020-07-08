import cv2
import numpy as np

# create a blank image 
img = np.zeros([512,512,3], dtype = np.uint8)

# Drawing lines
cv2.line(img,(0,0),(300,300), (0, 255, 0),3)

# draw a diagonal line

cv2.line(img,(0,0),(img.shape[1], img.shape[1]),(0,255,0),3)

cv2.imshow("Blank Image", img)
cv2.waitKey(0)
