"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Cleo Barmes.
  Winter term, 2018-2019.
"""
import rosebot
import time

def m3_beep_proximity(initial, delta, speed):
    robot = rosebot.RoseBot()
    ps = robot.sensor_system.ir_proximity_sensor
    b = robot.sound_system
    robot.drive_system.go(speed,speed)
    while ps.get_distance_in_inches() > 4:
        rate = initial + delta / ps.get_distance_in_inches()
        b.beep_number_of_times(2)
        time.sleep(rate)
    robot.drive_system.stop()

def m3_beep_retrieve(direction,speed):
    robot = rosebot.RoseBot()
    d=robot.drive_system
    c= robot.sensor_system.camera
    if direction == "CW":
        d.spin_clockwise_until_sees_object(speed,200)
    elif direction == "CCW":
        d.spin_counterclockwise_until_sees_object(speed,200)
    d.stop()
    camera_aim()
    m3_beep_proximity(1,0.1,speed)