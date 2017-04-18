import cv2
import numpy as np
import time
import sqlite3
import os.path
import subprocess

idINcre = 0 # this is for detecting Unknowns
KnINcre = 0 #Known Increment

timeout = time.time() + 1*5    # 10 sec -- Servo
timeouts = timeout
timelogic = 0

KnTimeout = time.time() + 1*8
KnTimeouts = KnTimeout
KnTimelogic = 0

UnknownTimeout = time.time() + 1*20    # 20 sec -- to SEND SMS, First SMS take 40 Sec
UnknownTimeouts = UnknownTimeout
UnknownTimeLogic = 1

IncTimeout = time.time() + 1*25
IncTimeouts = IncTimeout
IncTimeLogic = 0

def CapUnknown():
    #cam = cv2.VideoCapture(0)
    incr = 0

    path = "Unknown-Images/dropbox-home/"
    num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

    num_files = str(num_files)
    s, im = cam.read()
    cv2.imwrite("Unknown-Images/dropbox-home/Unknown."+(num_files) +'.'+ str(incr) + ".jpg", im)

#time related
def deftime():

    if timeout == timeouts:
        test = 0
        test = test - 1
        if test == 5 or time.time() > timeout:
            print "Shuja -->" # call to curl

            #subprocess.check_output(["curl", "http://localhost:8081"])

            resettime(0)
            print timeout

#time related
def resettime(para):

    global timeout, timeouts  #read python docs  #adata athi
    #timeout = para

    timeout = time.time() + 1*5    # 30 sec -- Servo
    timeouts = timeout

def UnknownSMSTime():
    global UnknownTimeLogic

    if UnknownTimeLogic == 0:

        CMDvar = subprocess.check_output(["curl", "-X", "POST", "-F", "'your_name=shuja'", "http://localhost:8081"])
        print CMDvar

        UnknownTimeLogic = 1

    if UnknownTimeout == UnknownTimeouts:
        test = 0
        test = test - 1
        if test == 5 or time.time() > UnknownTimeout:

            UnknownTimeLogic = 0
            resettime(0)
            print UnknownTimeout, "Unknown Timeout"

            ResetUnknownSMSTime()

def ResetUnknownSMSTime():

    global UnknownTimeout, UnknownTimeouts

    UnknownTimeout = time.time() + 1*20
    UnknownTimeouts = UnknownTimeout

def ResetUnknownIncre():
    global idINcre
    if IncTimeout == IncTimeouts:
        test = 0
        test = test -1
        if test == 5 or time.time() > IncTimeouts:
            idINcre = 0
            ResetUnknownIncreTime()

def ResetUnknownIncreTime():
    global IncTimeout, IncTimeouts

    IncTimeout = time.time() + 1*25
    IncTimeouts = IncTimeout

def ResetKnownIncre():
    global KnINcre
    if(KnINcre == 2):
        KnINcre = 0

    if KnTimeout == KnTimeouts:
        test = 0
        test = test -1
        if test == 5 or time.time() > KnTimeouts:
            KnINcre = 0
            ResetKnownIncreTime()

def ResetKnownIncreTime():
    global KnTimeout, KnTimeouts

    KnTimeout = time.time() + 1*8
    KnTimeouts = KnTimeout

    resettime(0)

    print "Known Reset"

def getProfile(Id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID="+str(Id)
    cursor = conn.execute(cmd)
    Profile = None

    for row in cursor:
        Profile = row

    conn.close()
    return Profile


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

        Profile = getProfile(Id)

        #Define Users

        #if(conf<50):
        #    if(Id==1):
        #        Id="Shuja"
        #        deftime()

        #    elif(Id==2):
        #        Id="Shimaz"

            #add elif statements for each user

        #else:
        #    Id="Unknown"

        if(conf<50):
            if(Profile != None):
                cv2.cv.PutText(cv2.cv.fromarray(im),Profile[1], (x,y+h),font, 255)
                KnINcre = KnINcre + 1
                #print Profile[0]
                print KnINcre, " Known"

                ResetKnownIncre()

                if(KnINcre == 1):
                    deftime()
                #print conf

        else:
            Id="Unknown"
            if(Id == "Unknown"):
                idINcre = idINcre + 1
                print idINcre, " Unknown"
                ResetUnknownIncre()
                if(idINcre == 50):
                    CapUnknown()
                    UnknownSMSTime()

                    idINcre = 0

        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)

    cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
