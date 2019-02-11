"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Ethan Mahn.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def real_thing():
    robot=rosebot.RoseBot()
    receiver = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()
    while receiver.leave == False: #must end to quit
        time.sleep(0.01)


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    drive_distance_tests()
    sound_tests()
    arm_tests()
    # drive_color_tests()
    #     Color tests are [Black, Red, Brown, White]

def sound_tests():
    beep_tests()
    tone_tests()
    speak_tests()

def beep_tests():
    robot = rosebot.RoseBot()
    robot.sound_system.beep_number_of_times(3)
    time.sleep(.2)
    robot.sound_system.beep_number_of_times(1)
    time.sleep(.2)
    robot.sound_system.beep_number_of_times(2)
    print("Beep test successful!")

def tone_tests():
    robot = rosebot.RoseBot()
    robot.sound_system.play_tone(500,300)
    time.sleep(.2)
    robot.sound_system.play_tone(1000,100)
    time.sleep(.2)
    robot.sound_system.play_tone(600, 500)
    print("Tone test successful!")

def speak_tests():
    robot = rosebot.RoseBot()
    robot.sound_system.speak("Good morning!")
    time.sleep(1.5)
    robot.sound_system.speak("Testing")
    time.sleep(1)
    robot.sound_system.speak("Test finished")
    print("Speak test successful!")

def drive_distance_tests():
    drive_for_seconds_tests()
    drive_for_inches_time_tests()
    drive_for_inches_encoder_tests()

def drive_for_inches_encoder_tests():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_encoder(2,-30)
    robot.drive_system.go_straight_for_inches_using_encoder(7, 70)
    robot.drive_system.go_straight_for_inches_using_encoder(8, -100)
    print("Drive for inches-encoder successful!")

def drive_for_inches_time_tests():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_time(8,100)
    robot.drive_system.go_straight_for_inches_using_time(7, -70)
    robot.drive_system.go_straight_for_inches_using_time(2, 30)
    print("Drive for inches-time successful!")

def drive_for_seconds_tests():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_seconds(4,100)
    robot.drive_system.go_straight_for_seconds(6, -60)
    robot.drive_system.go_straight_for_seconds(7, 43)
    print("Drive for seconds successful!")

def drive_color_tests():
    run_drive_greater_intensity_tests()
    run_drive_lesser_intensity_tests()
    run_drive_color_tests()

def run_drive_greater_intensity_tests():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_greater_than(45,100)

def run_drive_lesser_intensity_tests():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_less_than(30,35)

def run_drive_color_tests():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_color_is("Black",50)
    robot.drive_system.go_straight_until_color_is_not("Black", 50)
    robot.drive_system.go_straight_until_color_is("Red", 50)
    robot.drive_system.go_straight_until_color_is_not("Red", 50)
    robot.drive_system.go_straight_until_color_is("Brown", 50)
    robot.drive_system.go_straight_until_color_is_not("Brown", 50)
    robot.drive_system.go_straight_until_color_is("White", 50)
    robot.drive_system.go_straight_until_color_is_not("White", 50)

def arm_tests():
    run_test_calibrate_arm()
    time.sleep(2)
    run_test_arm()
    time.sleep(2)
    run_test_move_arm_to_position()

def run_test_calibrate_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    print("Calibration successful!")

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()
    print("Raise arm successful!")
    time.sleep(2)
    robot.arm_and_claw.lower_arm()
    print("Lower arm successful!")

def run_test_move_arm_to_position():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(360*10)
    print("Position 1 finished")
    time.sleep(.5)
    robot.arm_and_claw.move_arm_to_position(360*4)
    print("Position 2 finished")
    time.sleep(.5)
    robot.arm_and_claw.move_arm_to_position(360*7)
    print("Position 3 finished")
    time.sleep(.5)
    robot.arm_and_claw.lower_arm()
    print("Testing finished")


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
# main()
real_thing()