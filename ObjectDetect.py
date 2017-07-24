#Purpose: To detect if an object exists in front of the robot and if so 
#follow the object while maintaining a certain distance

import time
import Robot
import RPi.GPIO as GPIO
#Sensor intitialization
GPIO.setmode(GPIO.BCM)

#Right Sensor
TRIGR = 23
ECHOR = 24

GPIO.setup(TRIGR, GPIO.OUT)
GPIO.setup(ECHOR, GPIO.IN)
GPIO.output(TRIGR, False)
#Left Sensor
TRIGL = 20
ECHOL = 21

GPIO.setup(TRIGL, GPIO.OUT)
GPIO.setup(ECHOL, GPIO.IN)
GPIO.output(TRIGL, False)
#Forward Sensor
TRIGF = 17
ECHOF = 18

GPIO.setup(TRIGF, GPIO.OUT)
GPIO.setup(ECHOF, GPIO.IN)
GPIO.output(TRIGF, False)

print("Distance Measurement In Progress... ")

print("Waiting For Sensor To Settle")
time.sleep(2)

#Adjust motor offset so wheels turn at same speed
LEFT_TRIM = 0
RIGHT_TRIM = -2

#Create robot object to use functions from Robot class
robot = Robot.Robot(left_trim = LEFT_TRIM, right_trim = RIGHT_TRIM,left_id = 1, right_id = 3)

#Calculate distance to object in front of the sensor           
def distance(trigger,echo):
   #Emit 10 usec pulse
    GPIO.output(trigger,True)
    time.sleep(0.00001)
    GPIO.output(trigger,False)

    pulse_start = time.time()
    pulse_end = time.time()
    #Record time for return echo
    while GPIO.input(echo)== 0:
        pulse_start = time.time()       
    while GPIO.input(echo)== 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    #print(distance)
    return distance

def follow():
    lengthf = distance(TRIGF,ECHOF)
    lengthr = distance(TRIGR,ECHOR)
    lengthl = distance(TRIGL, ECHOL)
    try:
        while True:
            while lengthf > 20:
                robot.forward(150)
                length = 0
                for x in range(2):
                    lengthf =(lengthf + distance(TRIGF, ECHOF))/2.0
                print("ONWARD")
                print(length)
                time.sleep(.05)
            while lengthf <= 20 or lengthf >= 200:
                robot.stop()
                length = 0
                for x in range(2):
                    lengthf = (lengthf + distance())/2.0
                print(length)
                time.sleep(.05)
    except KeyboardInterrupt:
        robot.stop()
        print("Robot stopped by user")
       

if __name__ == '__main__':
    try:
        print("Measuring")
        while True:
            dist = distance()
            time.sleep(.5)
            if dist <= 20:
                follow()
                dist = distance()
                print("Measured Distance = %.1f cm" % dist)
                time.sleep(.5)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()



