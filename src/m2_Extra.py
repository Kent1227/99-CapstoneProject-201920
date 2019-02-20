#
# This is the beginning of Eddie's Extra file for the Final  Capstone Project
# The idea behind this design is to make an accurate representation of a Rose-Hulman Student
#


# The rosebot import was added in order for me to use the dot trick
import rosebot
import time


# def beep_proxy(robot, initial, delta, speed):
#    ps = robot.sensor_system.ir_proximity_sensor
#    b = robot.sound_system
#    robot.drive_system.go(int(speed),int(speed))
#    while ps.get_distance_in_inches() > 2:
#        rate = float(initial) + float(delta) / float(ps.get_distance_in_inches())
#        b.beep_number_of_times(2)
#        time.sleep(1 / rate)
#    robot.drive_system.stop()
#    robot.arm_and_claw.raise_arm()
#
#
# def beep_retrieve(robot, direction, speed):
#    d = robot.drive_system
#    if direction == "CW":
#        d.spin_clockwise_until_sees_object(int(speed), 100)
#    elif direction == "CCW":
#        d.spin_counterclockwise_until_sees_object(int(speed), 100)
#    d.stop()
#    camera_aim()
#    beep_proxy(robot, 1, 0.1, int(speed))
#
#
# def camera_aim():
#    robot = rosebot.RoseBot()
#    d = robot.drive_system
#    c = robot.sensor_system.camera
#    while True:
#        print(c.get_biggest_blob().center.x)
#        while c.get_biggest_blob().center.x > 170:
#            d.go(-20, 20)
#            print(c.get_biggest_blob().center.x)
#        d.stop()
#        while c.get_biggest_blob().center.x < 160:
#            d.go(20, -20)
#            print(c.get_biggest_blob().center.x)
#        d.stop()
#        if 160 < c.get_biggest_blob().center.x < 170:
#            break


# Not sure which find homework will work better, if they work at all
# The one below uses the object mode


def find_homework(robot):
    # robot.arm_and_claw.lower_arm()
    # robot.drive_system.pivot_left(50, 5)
    robot.drive_system.go_forward_until_distance_is_less_than(5, 50)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go_straight_for_inches_using_encoder(3, 50)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_straight_for_inches_using_encoder(6, 50)
    robot.drive_system.stop()
    robot.sound_system.speak("DEATH TO ALL HOMEWORK!")


# The one below uses the color mode
# The one above does indeed work better
# Do not use the one below


#######################################################################
# def find_homework2(robot):
    # robot.drive_system.spin_clockwise_until_sees_color(100, "White")
    # robot.drive_system.go_forward_until_distance_is_less_than(7, 100)
    # robot.drive_system.stop()
    # robot.arm_and_claw.raise_arm()
    # robot.drive_system.go_straight_for_inches_using_encoder(6, 100)
    # robot.arm_and_claw.lower_arm()
    # robot.drive_system.go_straight_for_inches_using_encoder(4, 50)
    # robot.drive_system.stop()
    # robot.sound_system.speak("DEATH TO ALL HOMEWORK!")
#######################################################################


def find_games(robot):
    # robot.arm_and_claw.lower_arm()
    # robot.drive_system.spin_clockwise_until_sees_object(25, 1)     # Need the area of a game box
    robot.drive_system.go_forward_until_distance_is_less_than(2, 50)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_left(100, 5)
    time.sleep(5)
    robot.drive_system.stop()
    robot.sound_system.speak("I LOVE VIDEO GAMES! I think I will go play some right now.")
    time.sleep(6)
    robot.drive_system.go_straight_for_inches_using_encoder(12, 50)
    robot.drive_system.stop()
    robot.drive_system.pivot_right(100, 5)
    time.sleep(5)
    robot.drive_system.stop()
    robot.sound_system.speak("Well, maybe I should do my homework.")
    time.sleep(4)
    robot.drive_system.pivot_left(100, 5)
    time.sleep(5)
    robot.drive_system.stop()
    robot.sound_system.speak("Nah, I will do it later.")
    time.sleep(4)
    robot.drive_system.go_straight_for_inches_using_encoder(12, 100)
    robot.arm_and_claw.lower_arm()


def find_food(robot):
    # robot.arm_and_claw.lower_arm()
    # robot.drive_system.spin_clockwise_until_sees_object(25, 1)     # Need the area of some type of food item
    robot.drive_system.go_forward_until_distance_is_less_than(2, 50)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_left(100, 5)
    time.sleep(5)
    robot.drive_system.stop()
    robot.sound_system.speak("Oh my God I am literally so hungry I haven't eaten in over 15 minutes")
    time.sleep(7)
    robot.drive_system.go_straight_for_inches_using_encoder(6, 50)
    robot.drive_system.pivot_right(100, 5)
    time.sleep(5)
    robot.drive_system.stop()
    robot.sound_system.speak("Where is the nearest microwave?")
    time.sleep(3)
    robot.arm_and_claw.lower_arm()


def go_to_sleep(robot):
    # robot.arm_and_claw.lower_arm()
    robot.sound_system.speak("Well, it has been a long day. Time to get some sleep.")
    time.sleep(5)
    robot.drive_system.go_straight_until_color_is("White", 50)     # May need to add a different color, not sure yet
    robot.drive_system.stop()
    robot.drive_system.pivot_left(100, 5)
    time.sleep(5)
    robot.drive_system.stop()
    robot.sound_system.speak("I sure hope they have Chicken Strips for lunch tomorrow.")
    time.sleep(6)
    snore(robot, 3)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_left(100, 5)
    time.sleep(5)
    robot.drive_system.stop()
    robot.sound_system.speak("OH MY LORD I FORGOT ABOUT MY HOMEWORK DUE AT MIDNIGHT OH NO PLEASE NO WHY ME!")
    time.sleep(7)
    robot.drive_system.go_straight_for_inches_using_encoder(24, 100)
    robot.arm_and_claw.lower_arm()


def snore(robot, num_of_snores):
    for _ in range(num_of_snores):
        robot.sound_system.speak("Snore")
        time.sleep(2)


def play_tone(robot):
    robot.sound_system.play_tone(500, 440)
