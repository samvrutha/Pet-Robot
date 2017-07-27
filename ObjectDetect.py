#Purpose: To detect if an object exists in front of the robot and if so 
#follow the object while maintaining a certain distance

import time
import Robot
import RPi.GPIO as GPIO
#Sensor intitialization
GPIO.setmode(GPIO.BCM)

#Right Sensor
TRIGR = 22
ECHOR = 23

GPIO.setup(TRIGR, GPIO.OUT)
GPIO.setup(ECHOR, GPIO.IN)
GPIO.output(TRIGR, False)
#Left Sensor
TRIGL = 19
ECHOL = 20

GPIO.setup(TRIGL, GPIO.OUT)
GPIO.setup(ECHOL, GPIO.IN)
GPIO.output(TRIGL, False)
#Forward Sensor
TRIGF = 5
ECHOF = 6

GPIO.setup(TRIGF, GPIO.OUT)
GPIO.setup(ECHOF, GPIO.IN)
GPIO.output(TRIGF, False)

print("Distance Measurement In Progress... ")

print("Waiting For Sensor To Settle")
time.sleep(2)

#Adjust motor offset so wheels turn at same speed
LEFT_TRIM = 0
RIGHT_TRIM = -1

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
       
def followrl(distf,distr,distl):
    y = 1
    while  True:
        if distf > 20 and distr > 50 and distl > 50 :
            robot.forward(125)
            print("FORWARD")
        elif distr < 50 and distr > 4 and distf > 10:
            robot.right(125)
            print("RIGHT")
        elif distl < 50 and distl > 4 and distf > 10:
            robot.left(125)
            print("LEFT")
        else:
            robot.stop()
            print("STOP")
        distf, distr,distl  = 0,0,0
        for x in range(y):
            distf =(distf + distance(TRIGF, ECHOF))/y
            distr =(distr + distance(TRIGR, ECHOR))/y
            distl =(distl + distance(TRIGL, ECHOL))/y
        print("FORWARD DISTANCE:  %.1f cm \t RIGHT DISTANCE: %.1f cm \t LEFT DISTANCE: %.1f cm"  %(distf ,distr, distl) )
                

if __name__ == '__main__':
    try:
        print("Measuring")
        dist = distance(TRIGF, ECHOF)
        distr= distance(TRIGR, ECHOR)
        distl = distance(TRIGL, ECHOL)
       #Measure distance but do not move until initialized
        while dist > 20:
            dist = distance(TRIGF, ECHOF)
            distr= distance(TRIGR, ECHOR)   
            distl = distance(TRIGL, ECHOL)
            print("FORWARD DISTANCE:  %.1f cm \t RIGHT DISTANCE: %.1f cm \t LEFT DISTANCE: %.1f cm"  %(dist ,distr, distl) )
            time.sleep(1)

           
        followrl(dist, distr, distl)
                

            
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()



