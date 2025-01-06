#from faceTracker import *
import self as self

from ledControl import *
#from servoControl import*
from FaceTrackerV1 import *
import time 

class myface(object):
        

    def start(self):
    
        ledControl.greenEyes(0,0,0,100)

  

        FaceTrackerV1.captureFace(self)


    start(self)

    ledControl.blueEyes(0,100,0,0)   
    ledControl.redEyes(0,0,100,0)

    


#faceTracker = faceTracker(blueEyes())



#changePositionToStart()



#greenEyes = greenEyes()








        