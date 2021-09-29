'''
This file also contains some code to do the same thing but instead for a face, to do this you'd have to download the haarcascade for that
'''
import cv2
 #also, learn how to train your own, they have a builtin function for this and that'd be cool
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = eye_cascade.detectMultiScale(gray, 1.5, 4)
    for x, y, w, h in faces:
        eyes = cv2.resize(frame[y:y+h, x:x+h], (200, 200))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("your eyes", eyes)
    
    cv2.imshow("You", frame)
    if cv2.waitKey(60) == ord('`'):
        break

cv2.destroyAllWindows()



# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# faces = face_cascade.detectMultiScale(gray, 1.5, 4)
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
# cv2.imshow('img', image)
#
# while True:
#     if cv2.waitKey(60) == ord('`'):
#         break
# cv2.destroyAllWindows()
