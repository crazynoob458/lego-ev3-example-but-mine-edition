#!/usr/bin/env pybricks-micropython 

""" 
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program 
----------------------------------------------------------------- 

""" 

# IMPORT SECTION 

# Here, we import the code that interacts with our Lego EV3 Bricks 

# We need to import all the devices we might plug in and use (eg: Motors and sensors) 

# Your robot won't run properly without importing these things 

from pybricks.hubs import EV3Brick 
from pybricks.ev3devices import Motor 
from pybricks.parameters import Port, Stop, Direction, Button, Color 
from pybricks.tools import wait, StopWatch, DataLog 
from pybricks.robotics import DriveBase 

 

# SETUP SECTION 
# Initialize the EV3 Brick. 

# We'll call  "brick" every time we want the brick to do something 
brick = EV3Brick() 

 

# Initialize the motors. 
left_motor = Motor(Port.B) 
right_motor = Motor(Port.C) 

 

# Initialize the drive base. 
# The DriveBase function will set up the driving mechanic to move both wheels together 
# We just need to say which motors we want to use as well as the wheels and the axle track 
# We'll call "robot" every time we want the robot to move 
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114) 

 

# START ROBOT SECTION 
# Now that we're all set up, let's tell the robot what to do! 
# Let's make it beep, wait 2 seconds, and then beep again so we know it's ready 

# DRIVING SECTION 
#Below are some examples of driving commands to move the robot 
#Delete the "#" for the driving commands you want to use 
 
# ----- Going Straight ----- 
# robot.straight(10) 
robot.drive_time(999, 0, 999999999) 