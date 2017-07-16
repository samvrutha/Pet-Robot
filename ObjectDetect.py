#Purpose: To detect if an object exists in front of the robot and if so 
#follow the object while maintaining a certain distance

import time
import Robot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Distance Measurement In Progress... ")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#GPIO.output(TRIG, False)

#print("Waiting For Sensor To Settle")
#time.sleep(2)

def distance():

    #Emit 10 usec pulse
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    pulse_start = time.time()
    pulse_end = time.time()
    #Record time for return echo
    while GPIO.input(ECHO)== 0:
        pulse_start = time.time()         
    while GPIO.input(ECHO)== 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    return distance
if __name__ == '__main__':
    try:
        print("Measuring")
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

#Adjust motor offset so wheels turn at same speed
#LEFT_TRIM = 0
#RIGHT_TRIM = -2
#Create robot object to use functions from Robot class
#robot = Robot.Robot(left_trim = LEFT_TRIM, right_trim = RIGHT_TRIM,left_id = 1, right_id = 3)


