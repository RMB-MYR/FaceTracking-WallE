import time
from time import sleep
import RPi.GPIO as GPIO
from servoMotor import servoMotor


class servoControl:
    angle = 1
    Movement = 0.1
    X=6.35
    Y=5.5
    
    servoX = servoMotor(7, X)
    servoY = servoMotor(8, Y)
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        
    def changePosition(face, targetX, targetY):
        if targetX > face.x + (face.w / 2) + 20:
            self.X = self.X + self.Movement
        elif targetX < face.x + (face.w / 2) - 20:
            self.X = self.X - self.Movement
        servoX.changePosition(self.X)
        
        if targetY > face.y + (face.h / 2) + 10:
            self.Y = self.Y + self.Movement
        elif targetY < face.y + (face.h / 2) - 10:
            self.Y = self.Y - self.Movement
        servoY.changePosition(self.Y)
     
    def changePositionToStart (self, X,Y):
        servoX.changePositionToStart(X)
        servoY.changePositionToStart(Y)
        
        
