import numpy as np
import serial
import time
import sys
import cv2
import face_recognition
arduino=serial.Serial('COM5',9600)
time.sleep(2)
print("Connection to arduino...")
xset=set()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

af=0
pf=0
tf=0
while 1:
    ret, img = cap.read()
    cv2.resizeWindow('img', 500,500)
    cv2.line(img,(500,250),(0,250),(0,255,0),1)
    cv2.line(img,(250,0),(250,500),(0,255,0),1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        arr = {y:y+h, x:x+w}
        print (arr)
        
        print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))

        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2

        print (xx)
        print (yy)

        center = (xx,yy)

        print("Center of Rectangle is :", center)
        cv2.imwrite('abc.jpg',gray)
    known_img=face_recognition.load_image_file("abc.jpg")
    unknown=face_recognition.load_image_file("bond.jpg")
    benc=face_recognition.face_encodings(known_img)
    if len(benc)>0:
        b_enc=benc[0]
    else:
        print("No face found")
        
    unenc=face_recognition.face_encodings(unknown)[0]
    results=face_recognition.compare_faces([b_enc],unenc)
    if results[0] == True:
        if(pf==0):
            arduino.write("Poovish is present".encode())
            pf=1
            xset.add("37")
    unknown=face_recognition.load_image_file("aish.jpg")
    unenc=face_recognition.face_encodings(unknown)[0]
    results=face_recognition.compare_faces([b_enc],unenc)
    if results[0] == True:
        
        if(af==0):
            arduino.write("Aish is present".encode())
            af=1
            xset.add("3")
    
    print(xset)
    cv2.imshow('img',img)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        xset.clear()
        arduino.write("end".encode())
        time.sleep(2)
        af=pf=tf=0
        break
