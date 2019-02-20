"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop, for compatibility with delegate).
  Author:  Ethan Mahn.
  Winter term, 2018-2019.
"""

import rosebot
import time
import math

# Chess functions

# Primary action functions
def chess_commands(commands):
    """Interprets the input commands and makes the robot execute them."""
    robot = rosebot.RoseBot()
    d = robot.drive_system
    space = 8 #FixMe space size
    for k in range(len(commands)):
        if commands[k] == "straight":
            d.go_true(space)
        elif commands[k] == "left":
            d.turn_degrees(-90)
        elif commands[k] == "right":
            d.turn_degrees(90)
        elif commands[k] == "reverse":
            d.turn_degrees(180)
def pick_up():
    """Runs the commands to make the robot pick up a piece."""
    robot = rosebot.RoseBot()
    if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 7: #Fixme distance for piece missing
        print("No piece!")
    else:
        robot.drive_system.go_forward_until_distance_is_less_than(2, 30) #FixMe distance to grab at
        robot.arm_and_claw.raise_arm()
        robot.drive_system.go_straight_until_intensity_is_in_range(50,80,50) #FixMe intensity of circle
        robot.drive_system.go_true(2) #FixMe distance to center robot
def put_down():
    """Runs the commands to make the robot place a piece."""
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_in_range(50, 80, 50) #FixMe intensity of circle
    robot.drive_system.go_true(-5) #FixMe backup distance
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_straight_until_intensity_is_in_range(50, 80, -50) #FixMe intensity of circle
    robot.drive_system.go_true(2) #FixMe distance to center robot
def dispose():
    """Runs the commands to make the robot drop a captured piece off the board."""
    robot = rosebot.RoseBot()
    robot.drive_system.go_true(5) #FixMe dropoff distance
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_true(-5) #FixMe dropoff distance, make circle?

# Support functions
def robot_lost():
    """Finds the center of the space the robot is in, and re-orients it facing up."""
    robot = rosebot.RoseBot()
    d = robot.drive_system
    c = robot.sensor_system.color_sensor
    d.go(0, 70) #FixMe speed of wander
    while True:
        if c.get_reflected_light_intensity() < 20 : #FixMe intensity of border
            d.go_straight_for_inches_using_encoder(2,-100) #FixMe backup distance
            d.go(0, 70) #FixMe speed of wander
        elif c.get_reflected_light_intensity() < 70: #FixMe intensity of circle
            time.sleep(0.2) #FixMe wait before stop time
            break
    d.go_true(2) #FixMe distance to center robot
    d.go(50,-50) #FixMe speed of turn
    while c.get_reflected_light_intensity() > 70: #FixMe intensity of orientation bar
        pass
    d.stop()
    # update robopos #FixMe send message to pc
def locate_robot():
    """Finds the position of the robot on the board by triangulation with the two reference towers."""
    robot = rosebot.RoseBot()
    d = robot.drive_system
    d.spin_clockwise_until_sees_object(30,100) #FixMe find first speed, area
    start = time.time()
    d.go(-30,30) #FixMe search speed
    time.sleep(1) #FixMe time to lose first tower
    d.spin_clockwise_until_sees_object(30,100) #FixMe search speed
    t = time.time()-start
    d.stop()
    y, x = triangulation(t,robot)
    space = 8  # FixMe space size
    pos = [int((y / space)+.5)-1, int((x / space)+.5)-1, 0] #FixMe picking space
    return pos #FixMe send to pc
def triangulation(t,robot):
    """Does the triangulation calculations."""
    deg_per_sec = 20  # FixMe degrees per second searching
    camera_aim()
    ac = t * deg_per_sec
    if ac > 180:
        ac = 360 - ac
    a = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()+4 #FixMe distance from prox to center
    c = 85  # FixMe distance between towers (80 to edge, need center offset)
    b = (math.cos(ac) * a) + math.sqrt(((math.cos(ac) ** 2) * (a ** 2)) - (a ** 2) + (c ** 2))
    ab = math.asin((b * math.sin(ac) / c))
    y = b * math.cos(ab)
    x = b * math.sin(ab)
    return y, x
def calibrate_degpersec():
    d = rosebot.RoseBot().drive_system
    start = time.time()
    d.turn_degrees()
    t = time.time() - start
    print("Time:", t)




# Basic functions
def m4_led_proximity(initial,delta,speed):
    robot = rosebot.RoseBot()
    ps = robot.sensor_system.ir_proximity_sensor
    l = robot.led_system
    robot.drive_system.go(speed,speed)
    while ps.get_distance_in_inches() > 2:
        rate = float(initial)+(float(delta)/ps.get_distance_in_inches())
        cycle_leds(rate,l)
    time.sleep(0.2)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
def cycle_leds(rate,led):
    for k in range(4):
        if k == 0:
            led.left_led.turn_on()
            led.right_led.turn_off()
        elif k == 1:
            led.left_led.turn_off()
            led.right_led.turn_on()
        elif k == 2:
            led.left_led.turn_on()
            led.right_led.turn_on()
        else:
            led.left_led.turn_off()
            led.right_led.turn_off()
        time.sleep(1 / rate)
def m4_led_retrieve(direction,speed):
    robot = rosebot.RoseBot()
    d=robot.drive_system
    if direction == "CW":
        d.spin_clockwise_until_sees_object(int(speed),100)
    elif direction == "CCW":
        d.spin_counterclockwise_until_sees_object(int(speed),100)
    d.stop()
    camera_aim()
    m4_led_proximity(1,100,int(speed))
def camera_aim():
    robot = rosebot.RoseBot()
    d = robot.drive_system
    c = robot.sensor_system.camera
    while True:
        print(c.get_biggest_blob().center.x)
        while c.get_biggest_blob().center.x > 170:
            d.go(-20, 20)
            print(c.get_biggest_blob().center.x)
        d.stop()
        while c.get_biggest_blob().center.x < 160:
            d.go(20, -20)
            print(c.get_biggest_blob().center.x)
        d.stop()
        if 160 < c.get_biggest_blob().center.x < 170:
            break