#
#This is the beginning of Eddie's Extra file for the Final Project
#The idea behind this design is to make an accurate representation of a Rose-Hulman Student
#


import rosebot
import time


#def beep_proxy(robot, initial, delta, speed):
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
#def beep_retrieve(robot, direction, speed):
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
#def camera_aim():
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
    robot.drive_system.spin_clockwise_until_sees_object(25, 93)
    robot.drive_system.go_forward_until_distance_is_less_than(5, 100)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go_forward_until_distance_is_less_than(3, 100)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_straight_for_inches_using_encoder(4, 50)
    robot.drive_system.stop()
    robot.sound_system.speak("DEATH TO ALL HOMEWORK!")

# The one below uses the color mode
# The one above does indeed work better
# Do not use the one below


#######################################################################
#def find_homework2(robot):
    #robot.drive_system.spin_clockwise_until_sees_color(100, "White")
    #robot.drive_system.go_forward_until_distance_is_less_than(7, 100)
    #robot.drive_system.stop()
    #robot.arm_and_claw.raise_arm()
    #robot.drive_system.go_straight_for_inches_using_encoder(6, 100)
    #robot.arm_and_claw.lower_arm()
    #robot.drive_system.go_straight_for_inches_using_encoder(4, 50)
    #robot.drive_system.stop()
    #robot.sound_system.speak("DEATH TO ALL HOMEWORK!")
#######################################################################


def find_games(robot):
    robot.drive_system.spin_clockwise_until_sees_object(25, 1)     # Need the area of a game box
    robot.drive_system.go_forward_until_distance_is_less_than(3, 100)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_left(100, 5)
    robot.sound_system.speak("I love video games! I think I will go play some right now.").wait()
    robot.drive_system.go_straight_for_inches_using_encoder(12, 100)
    robot.drive_system.stop()
    robot.drive_system.pivot_right(100, 5)
    robot.sound_system.speak("Well, maybe I should do my homework.").wait()
    robot.drive_system.pivot_left(100, 5)
    robot.sound_system.speak("Nah, I will do it later.")
    robot.drive_system.go_straight_for_inches_using_encoder(12, 100)


def find_food(robot):
    robot.drive_system.spin_clockwise_until_sees_object(25, 1)     # Need the area of some type of food item
    robot.drive_system.go_forward_until_distance_is_less_than(3, 100)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_left(100, 5)
    robot.sound_system.speak("Oh my God I am literally so hungry I haven't eaten in over 15 minutes")
    robot.drive_system.go_straight_for_inches_using_encoder(12, 100)

