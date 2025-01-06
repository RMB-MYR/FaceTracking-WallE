import RPi.GPIO as GPIO


class LED:
    #Intitailisieren der LED
    
    lightItensity = 500
    
    
    def __init__(self, pin, LED_AB):
        
          
        GPIO.setup(pin, GPIO.OUT)
        self.LED = GPIO.PWM(pin, self.lightItensity)
        self.LED.start(LED_AB)
        
    



