import numpy as np
import cv2
import winsound
from playsound import playsound
import os


duration = 1000  # millisecond
freq = 440  # Hz
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_DUPLEX
font3 = cv2.FONT_HERSHEY_TRIPLEX

cap = cv2.VideoCapture(0)
count1 = [0]
count = count1[0]
status = prestatus = "OPEN"
dconstant = 30             #Drowsiness counter
countd = 0
cnt = 0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    max_f = 0

    for (x1,y1,w1,h1) in faces:
        if w1*h1 >= max_f:
            x = x1
            y = y1
            w = w1
            h = h1

    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
        
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 14)
    #mouth = mouth_cascade.detectMultiScale(roi_gray, 1.740, 25)    

    #for (ex,ey,ew,eh) in mouth:
    #        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    if len(eyes) == 0:
        if status == "OPEN":
            count += 1
        status = "CLOSED"
        cv2.putText(img, 'CLOSED',(int(x+w/7), int(y+h/6)), font1, 1.6, (255, 200, 255))
    else:
        if status == "CLOSED":
            count += 1
        status = "OPEN"
        cv2.putText(img, 'OPEN', (int(x+w/7), int(y+h/6)), font1, 1.6, (255, 200, 255))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    if(status == prestatus):
        if status == 'CLOSED':
            countd += 1
    if(status!=prestatus):
        if status == 'OPEN':
            countd = 0
    if countd>=dconstant:
        cv2.putText(img, 'WAKE UP!!!', (30, 90), font3, 3.5, (0, 0, 155))
        #winsound.MessageBeep(-1)
        #winsound.PlaySound('C:\Users\vishal\Desktop\vishal\OpenCV\Eye tracking\iste-eye-track\alarm.mp3', winsound.SND_ALIAS)
        #winsound.Beep(freq, duration)
        if cnt == 0:
            #print '\a'
            #winsound.MessageBeep(-1)
            os.system("start alarm.mp3")
        cnt += 1
        if cnt >= 100:
            cnt = 0
    cv2.putText(img, 'BLINKS:'+ str(int(count/2)),(int(x-w/4), int(y-h/4)+1), font2, 1.7, (255, 255, 255))
    cv2.imshow('img',img)
    prestatus = status
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
