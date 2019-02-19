"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Cleo Barmes.
  Winter term, 2018-2019.
"""
import rosebot
import time
import m4_extra as m4

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


def m3_baby_walk(speed, progress_state):
    robot = rosebot.RoseBot()
    d = robot.drive_system
    ps = robot.sensor_system.ir_proximity_sensor
    c = robot.sensor_system.camera
    a = robot.arm_and_claw
    s = robot.sound_system
    d.go_forward_until_distance_is_less_than(3, speed)
    for k in range(2):
        a.move_arm_to_position(5000)
        a.move_arm_to_position(4000)
        s.speak("WAHHHH WAHHH")
        time.sleep(2)
        s.speech_maker.speak("goo goo ga ga")
    a.lower_arm()

    m3_find_bottle(speed, progress_state)

# I used (m4)Ethan's  led retrieve code as my base, but due to some desired functions,
# the code needed to be altered.

def m3_baby_proximity(initial, delta, speed, progress_state):
    robot = rosebot.RoseBot()
    ps = robot.sensor_system.ir_proximity_sensor
    l = robot.led_system
    d = robot.drive_system
    robot.drive_system.go(speed, speed)
    while ps.get_distance_in_inches() > 2:
        rate = float(initial) + (float(delta) / ps.get_distance_in_inches())
        m4.cycle_leds(rate, l)

    time.sleep(0.2)
    d.stop()
    robot.arm_and_claw.raise_arm()


def m3_find_bottle(speed, progress_state):
    robot = rosebot.RoseBot()
    d = robot.drive_system
    d.spin_counterclockwise_until_sees_object(int(speed), 100)
    d.stop()
    camera_aim()
    m3_baby_proximity(1, 100, int(speed), int(progress_state))



