"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop, for compatibility with delegate).
  Author:  Ethan Mahn.
  Winter term, 2018-2019.
"""

import rosebot
import time

def m4_led_proximity(initial,delta,speed):
    robot = rosebot.RoseBot()
    ps = robot.sensor_system.ir_proximity_sensor
    l = robot.led_system
    robot.drive_system.go(speed,speed)
    while ps.get_distance_in_inches() > 4:
        rate = initial+delta/ps.get_distance_in_inches()
        cycle_leds(rate,l)
    robot.drive_system.stop()

def cycle_leds(rate,led):
    while True:
        for k in range(3):
            if k == 0:
                led.left_led.turn_on()
            elif k == 1:
                led.left_led.turn_off()
                led.right_led.turn_on()
            elif k == 2:
                led.left_led.turn_on()
            else:
                led.left_led.turn_off()
                led.right_led.turn_off()
            time.sleep(rate)

def m4_led_retrieve(direction,speed):
    robot = rosebot.RoseBot()
    d=robot.drive_system
    c= robot.sensor_system.camera
    if direction == "CW":
        d.spin_clockwise_until_sees_object(speed,200)
    elif direction == "CCW":
        d.spin_counterclockwise_until_sees_object(speed,200)
    d.stop()
    camera_aim()
    m4_led_proximity(1,0.1,speed)

def camera_aim():
    robot = rosebot.RoseBot()
    d = robot.drive_system
    c = robot.sensor_system.camera
    while True:
        while c.get_biggest_blob().center.x() > 10:
            d.go(20, -20)
        d.stop()
        while c.get_biggest_blob().center.x() < -10:
            d.go(-20, 20)
        d.stop()
        if c.get_biggest_blob().center.x() < 10 and c.get_biggest_blob().center.x() > -10:
            break