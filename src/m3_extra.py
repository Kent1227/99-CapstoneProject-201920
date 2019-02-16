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
    robot.drive_system.go(int(speed),int(speed))
    while ps.get_distance_in_inches() > 2:
        rate = float(initial) + float(delta) / float(ps.get_distance_in_inches())
        b.beep_number_of_times(2)
        time.sleep(1 / rate)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()

def m3_beep_retrieve(direction,speed):
    robot = rosebot.RoseBot()
    d = robot.drive_system
    if direction == "CW":
        d.spin_clockwise_until_sees_object(int(speed),100)
    elif direction == "CCW":
        d.spin_counterclockwise_until_sees_object(int(speed),100)
    d.stop()
    camera_aim()
    m3_beep_proximity(1,0.1,int(speed))

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


def m3_baby_walk(speed):
    robot = rosebot.RoseBot()
    d = robot.drive_system
    ps = robot.sensor_system.ir_proximity_sensor
    c = robot.sensor_system.camera
    a = robot.arm_and_claw
    s = robot.sound_system
    d.go_forward_until_distance_is_less_than(3, speed)
    for k in range(5):
        s.speak("a-ga")
        a.move_arm_to_position(5000)
        time.sleep(1)
        a.move_arm_to_position(4000)
        a.lower_arm()
        s.speech_maker.speak("Wahhh")

    d.go(20, 10)
    time.sleep(5)

def m3_find_bottle(speed):
    pass

