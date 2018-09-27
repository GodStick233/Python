import face_recognition
import cv2
image = face_recognition.load_image_file('t3.jpg')
face_locations = face_recognition.face_locations(image)
img = cv2.imread('t3.jpg')
faceNum = len(face_locations)
for i in range(0, faceNum):
    top =  face_locations[i][0]
    right =  face_locations[i][1]
    bottom = face_locations[i][2]
    left = face_locations[i][3]
    start = (left, top)
    end = (right, bottom)
    color = (55,255,155)
    thickness = 2
    cv2.rectangle(img, start, end, color, thickness)
    newimg = img[top:bottom,left:right]
    #cv2.imwrite('1.jpg', newimg)
cv2.imshow('1',img)
cv2.waitKey(0)
