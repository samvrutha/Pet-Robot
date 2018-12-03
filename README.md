# Pet-Robot
#Pet Robot embedded systems project using Raspberry Pi. Robot will detect and follow person around room.

# Software Setup 
First clone the repository on your target device. 
```bash
$ git clone https://github.com/tsamvrutha/Pet-Robot.git
$ cd Pet-Robot
```

Next, install the Adafruit library for the motor-shield.
```bash
$ git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
$ cd Adafruit-Motor-HAT-Python-Library
$ sudo python setup.py install
```
For further instructions on downloading the motor shield and any necessary python dependencies see this website:  
https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software   

Next you will need to install CircuitPython in order to properly use the AMG88xx library.
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

Make sure to install RPi.GPIO and adafruit-blinka
```bash
$ pip3 install RPi.GPIO
$ pip3 install adafruit-blinka
```

Then install the AMG88xx library using. 
***NOTE*** CircuitPython is not supported on Python 2
 ```bash
 $ sudo pip3 install adafruit-circuitpython-amg88xx
# Hardware Setup
