#import required libraries
import time
import cv2

#if using the picamera, import those libraries as well
from picamera.array import PiRGBArray
from picamera import PiCamera


class FaceTrackerV1:
    cascPath = "haarcascade.xml"
    cameraWidth = 320
    cameraHeight = 240
    
    camera = PiCamera()
        
    def __init__(self):
        
        print('__init__ aaaaa' )
        
        #point to the haar cascade file in the directory
        faceCascade = cv2.CascadeClassifier(cascPath)

        #start the camera and define settings
        self.camera.resolution = (self.cameraWidth, self.cameraHeight) #a smaller resolution means faster processing
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(self.cameraWidth, self.cameraHeight))
        
        print('bbb')
        #Center of the Image
        center_x = int (160)
        center_y = int (120)
         

        #give camera time to warm up
        time.sleep(0.1)
    
    
    def captureFace():
              
        print('captureFace bbbbbb')
        
        # start video frame capture
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
        # take the frame as an array, convert it to black and white, and look for facial features
            image = frame.array
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
                )
         
        print('juhuuu') 