import cv2 
import time 
startTime=time.time()

def snapShot():
    cam=cv2.VideoCapture(0)

    result=True

    while result:
        startTime=time.time()
        ret,frame=cam.read()
        cv2.imwrite("test1.jpg",frame)

        result=False
    
    cam.release()

    cv2.destroyAllWindows()

while(True):
    if(time.time()-startTime<20):
        snapShot()