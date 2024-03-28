#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialize the EV3 brick
ev3 = EV3Brick()

# Initialize the motors
rightmotor = motor(port.B)
leftmotor = motor(port.C)

# Initialize the sensors
USsensor = UltrasonicSensor(Port.S4)
Csensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Go forward for one meter.
robot.straight(1000)

# Go backwards for one meter
robot.straight(-1000)

# Turn 360 degrees
robot.turn(360)

# Make the speaker beep
Ev3.speaker.beep()

# Get the data from Ultrasonic
datapoint1 = USsensor.distance()

# Get data from Colour
datapoint2 = line_sensor.reflection()