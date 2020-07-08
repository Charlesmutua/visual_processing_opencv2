import cv2

color = (255,255,0)

#Add Cascade = Process the image after reading it.

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Read the Image with the Face
img = cv2.imread("resources/faces.jpg")

# Resize the Image

resized = cv2.resize(img, (600, 400))



# Conver the Image to GreyScale

imgGray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

#Find the Faces
# Define the Scale factor
# Define the minimum neighbor

face = faceCascade.detectMultiScale(imgGray, 1.1, 4)


# Bounding box across detected face

# Looping over every single box

# Declare starting point and Corner points.



for (x,y,w,h) in face:
    # draw a box & write a text "face"
    cv2.rectangle(resized, (x,y), (x+w, y+h), color, 2)
    cv2.putText(resized,"face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 1)


cv2.imshow("Resized", resized)
cv2.waitKey(0)

