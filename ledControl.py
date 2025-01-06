import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
from LED import LED
from time import sleep

class ledControl:
    
    GPIO.setmode(GPIO.BOARD)
    
    def __init__(self):
        
        print('cccccc')   
        
        GPIO.setmode(GPIO.BOARD)
        
    
    def blueEyes(self,LED_AB,LED_AR,LED_AG):
                       
        LED_B = LED(13,LED_AB)
        LED_G = LED(15,LED_AG)
        LED_R = LED(11,LED_AR)
        sleep(0.5)
        
        
        #self.LED_B.start(LED_AB)
        #self.LED_R.stop(LED_AR)
        #self.LED_G.stop(LED_AG)
        #return
        #self.LED_B.start(100)
        #self.LED_R.stop(0)
        #self.LED_G.stop(0)
        

    def redEyes(self,LED_AB,LED_AR,LED_AG):
        LED_B = LED(13,LED_AB)
        LED_G = LED(15,LED_AG)
        LED_R = LED(11,LED_AR)
        sleep(0.5)
        
    def greenEyes(self,LED_AB,LED_AR,LED_AG):
        LED_B = LED(13,LED_AB)
        LED_G = LED(15,LED_AG)
        LED_R = LED(11,LED_AR)
        sleep(0.5)
        



        