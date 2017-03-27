import cv2
import numpy as np
import time

timeout = time.time() + 1*10    # 30 sec
timeouts = timeout
timelogic = 0

def deftime():

    if timeout == timeouts:
        test = 0
        test = test - 1
        if test == 5 or time.time() > timeout:
            print "Shuja" # call to curl
            resettime(0)
            print timeout

def resettime(para):

    global timeout, timeouts  #read python docs  #adata athi
    #timeout = para

    timeout = time.time() + 1*10    # 30 sec
    timeouts = timeout

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])

        #Define Users

        if(conf<50):
            if(Id==1):
                Id="Shuja"
                deftime()

            elif(Id==2):
                Id="Shimaz"

            #add elif statements for each user

        else:
            Id="Unknown"
        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
    cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
