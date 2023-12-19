import cv2

camera = cv2.VideoCapture(0) 

while True:
    ret, frame = camera.read()
    cv2.imwrite('image.jpg', frame)