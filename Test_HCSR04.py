#Purpose: Simple program to test proper functionality of the HCSR04 ultrasound device. Tests that distance can be measured and used to control motors.
import time
import Robot
import RPi.GPIO as GPIO 
from ObjectDetect import distance
GPIO.setmode(GPIO.BCM)

def follow(trig, echo):
    length = distance(trig, echo, robot)
    try:
        while True:
            while lengthf > 20:
                robot.forward(150)
                length = 0
                for x in range(2):
                    lengthf =(lengthf + distance(trig, echo))/2.0
                print("ONWARD")
                print(length)
                time.sleep(.05)
            while lengthf <= 20 or lengthf >= 200:
                robot.stop()
                length = 0
                for x in range(2):
                    lengthf = (lengthf + distance(trig, echo))/2.0
                print(length)
                time.sleep(.05)
    finally KeyboardInterrupt:
        robot.stop()
        print("Robot stopped by user")
        GPIO.cleanup()
