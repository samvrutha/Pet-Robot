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

Next, install RPi.GPIO. ***NOTE:*** This library will only be able to properly install on a Raspberry Pi device.
```bash
$ pip install RPi.GPIO
```

# Hardware Setup
