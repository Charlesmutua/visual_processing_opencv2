import numpy as np

import cv2

#img = np.zeros([300,300,3],dtype=np.uint8)
img = cv2.imread("resources/image3.jpg")


# Line
#cv2.line(img,(0,0), (300,300), (255,0,0), 5)

#Rectangle
cv2.rectangle(img, (10,10), (200,100),(0,255,0), 3)

#Circle
cv2.circle(img, (200,100), 100,(255,0,0), 6)



cv2.imshow("Draw on Image", img)
cv2.waitKey(0)

