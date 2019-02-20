"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop, for compatibility with delegate).
  Author:  Ethan Mahn.
  Winter term, 2018-2019.
"""

import rosebot
import time
import math


# import mqtt_remote_method_calls as com


# Chess functions

def chess_commands(commands, robot):
    """Interprets the input commands and makes the robot execute them."""
    print(commands)
    d = robot.drive_system
    space = 7  # FixMe space size
    for k in range(len(commands[0])):
        if commands[0][k] == "straight":
            print("0")
            d.go_straight_for_inches_using_encoder(space, 100)
        elif commands[0][k] == "left":
            print("3")
            d.turn_degrees(-90, 70)
        elif commands[0][k] == "right":
            print("1")
            d.turn_degrees(90, 70)
        elif commands[0][k] == "reverse":
            print("2")
            d.turn_degrees(190, 70)


def pick_up(robot):
    """Runs the commands to make the robot pick up a piece."""
    print("Pick up")
    # robot.drive_system.go_forward_until_distance_is_less_than(2, 30) #FixMe distance to grab at
    robot.arm_and_claw.raise_arm()
    # robot.drive_system.go_straight_until_intensity_is_in_range(50,80,50) #FixMe intensity of circle
    # robot.drive_system.go_straight_for_inches_using_encoder(2,30) #FixMe distance to center robot


def put_down(robot):
    """Runs the commands to make the robot place a piece."""
    print("Put down")
    # robot.drive_system.go_straight_until_intensity_is_in_range(50, 80, 50) #FixMe intensity of circle
    # robot.drive_system.go_straight_for_inches_using_encoder(5,-50) #FixMe backup distance
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_straight_for_inches_using_encoder(2, -70)
    # robot.drive_system.go_straight_until_intensity_is_in_range(50, 80, -50) #FixMe intensity of circle
    # robot.drive_system.go_straight_for_inches_using_encoder(5,50) #FixMe distance to center robot


def dispose(robot):
    """Runs the commands to make the robot drop a captured piece off the board."""
    print("Dispose")
    # robot.drive_system.go_straight_for_inches_using_encoder(5,50) #FixMe dropoff distance
    robot.arm_and_claw.lower_arm()
    # robot.drive_system.go_straight_for_inches_using_encoder(5,-50) #FixMe dropoff distance, make circle?


# Support functions
def robot_lost(robot, mqtt):
    """Finds the center of the space the robot is in, and re-orients it facing up."""
    d = robot.drive_system
    c = robot.sensor_system.color_sensor
    d.go(0, 100)  # FixMe speed of wander
    while True:
        if c.get_reflected_light_intensity() < 10:  # FixMe intensity of border
            print("wall")
            d.go(-70, 0)  # FixMe speed of wander
            time.sleep(1)  # FixMe backup time
            d.go(0, 70)  # FixMe speed of wander
        elif 10 < c.get_reflected_light_intensity() < 20:  # FixMe intensity of circle
            "circle"
            time.sleep(0.2)  # FixMe wait before stop time
            break
    d.go_straight_for_inches_using_encoder(1, 30)  # FixMe distance to center robot
    d.go(50, -50)  # FixMe speed of turn
    while c.get_reflected_light_intensity() > 40:  # FixMe intensity of orientation bar
        pass
    print("line")
    d.stop()
    # mqtt = start_mqtt()
    mqtt.send_message("update_orientation", [0])


def locate_robot():
    """Finds the position of the robot on the board by triangulation with the two reference towers."""
    robot = rosebot.RoseBot()
    d = robot.drive_system
    d.spin_clockwise_until_sees_object(70, 10)  # FixMe find first speed, area
    start = time.time()
    d.go(70, -70)  # FixMe search speed
    time.sleep(1)  # FixMe time to lose first tower
    d.spin_clockwise_until_sees_object(70, 10)  # FixMe search speed
    t = time.time() - start
    d.stop()
    y, x = triangulation(t, robot)
    space = 2  # FixMe space size
    pos = [int(y / space) - 3, int(x / space) - 1, 0]  # FixMe picking space
    print("y:", pos[0], "x:", pos[1])
    # mqtt = start_mqtt()
    # mqtt.send_message("update_location", [x, y])


def triangulation(t, robot):
    """Does the triangulation calculations."""
    deg_per_sec = 94.5  # FixMe degrees per second searching
    ac = t * deg_per_sec
    if ac > 180:
        ac = 360 - ac
        robot.drive_system.go(70, -70)  # FixMe search speed
        time.sleep(1)  # FixMe time to lose first tower
        robot.drive_system.spin_clockwise_until_sees_object(70, 10)  # FixMe search speed
    camera_aim()
    a = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() + 4  # FixMe distance from prox to center
    c = (8 * 8) + 0  # FixMe distance between towers (need center offset)
    b = (math.cos(ac) * a) + math.sqrt(((math.cos(ac) ** 2) * (a ** 2)) - (a ** 2) + (c ** 2))
    ab = math.asin((b * math.sin(ac) / c))
    y = math.fabs(a * math.cos(ab))
    x = math.fabs(a * math.sin(ab))
    print("angle:", ac, "y:", y, "x:", x)
    return y, x


# Basic functions
def m4_led_proximity(initial, delta, speed):
    robot = rosebot.RoseBot()
    ps = robot.sensor_system.ir_proximity_sensor
    l = robot.led_system
    robot.drive_system.go(speed, speed)
    while ps.get_distance_in_inches() > 2:
        rate = float(initial) + (float(delta) / ps.get_distance_in_inches())
        cycle_leds(rate, l)
    time.sleep(0.2)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()


def cycle_leds(rate, led):
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


def m4_led_retrieve(direction, speed):
    robot = rosebot.RoseBot()
    d = robot.drive_system
    if direction == "CW":
        d.spin_clockwise_until_sees_object(int(speed), 100)
    elif direction == "CCW":
        d.spin_counterclockwise_until_sees_object(int(speed), 100)
    d.stop()
    camera_aim()
    m4_led_proximity(1, 100, int(speed))


def camera_aim():
    robot = rosebot.RoseBot()
    d = robot.drive_system
    c = robot.sensor_system.camera
    while True:
        print(c.get_biggest_blob().center.x)
        while c.get_biggest_blob().center.x > 170:
            d.go(30, -30)
            print(c.get_biggest_blob().center.x)
        d.stop()
        while c.get_biggest_blob().center.x < 160:
            d.go(-30, 30)
            print(c.get_biggest_blob().center.x)
        d.stop()
        if 160 < c.get_biggest_blob().center.x < 170:
            break
