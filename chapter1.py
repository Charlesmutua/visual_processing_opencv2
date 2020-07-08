import cv2
print ("Package is installed")

"""
#read an image and display it

img = cv2.imread("resources/image1.jpg")

cv2.imshow("Image", img)

cv2.waitKey(0)

"""


# Read a video and display it
"""
cap = cv2.VideoCapture("resources/vid.mp4")

while True:
    success, img = cap.read()

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
"""

# How to read a webcam and display it
"""
webcam = cv2.VideoCapture(0)
# Define Width and Height
# 3 = width, 4 = height

webcam.set(3,640)
webcam.set(4,480)
while True:
    success, img = webcam.read()

    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    """

# converting an image to GrayScale.

img = cv2.imread("resources/image1.jpg")
cv2.imshow("Image Or", img)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", imgGray)

cv2.waitKey(0)
# Blur  = GaussianBlur()
# imgBlur = cv2.GaussianBlur(img, (3,9), 0)