import RPi.GPIO as GPIO



class servoMotor:
    GPIO.setmode(GPIO.BOARD)
    frequent = 50
    
    
    def __init__(self,pin, startPosition):
        GPIO.setup(pin, GPIO.OUT)
        self.servoMotor = GPIO.PWM(pin,self.frequent)
        self.servoMotor.start(startPosition)
        
    def changePosition(self, dutyCycle):
        self.servoMotor.ChangeDutyCycle(dutyCycle)