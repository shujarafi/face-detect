import cv2
import os.path


def CapUnknown():
    cam = cv2.VideoCapture(0)
    incr = 0

    path = "dropbox-home"
    num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

    num_files = str(num_files)
    s, im = cam.read()
    cv2.imwrite("dropbox-home/Unknown."+(num_files) +'.'+ str(incr) + ".jpg", im)

CapUnknown()

