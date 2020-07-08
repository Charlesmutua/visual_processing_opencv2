import cv2
img = cv2.imread("resources/image3.jpg")

# Line

cv2.line(img, (10,100), (100,100), (255,0,255), 4)


cv2.imshow("Draw on Image", img)
cv2.waitKey(0)