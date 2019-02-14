"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Cleo Barmes.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    tests()

def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_reciever = com.MqttClient(delegate)
    mqtt_reciever.connect_to_pc()
    while delegate.leave == False: #must end to quit
        time.sleep(0.01)


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


def m3_led_proximity(initial,delta,speed):
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

def m3_led_retrieve(direction,speed):
    robot = rosebot.RoseBot()
    d=robot.drive_system
    c= robot.sensor_system.camera
    if direction == "CW":
        d.spin_clockwise_until_sees_object(speed,200)
    elif direction == "CCW":
        d.spin_counterclockwise_until_sees_object(speed,200)
    d.stop()
    camera_aim()
    m3_led_proximity(1,0.1,speed)

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

def tests():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    print("Tests started!")
    drive_proximity_tests()
    drive_camera_tests()
    # drive_distance_tests()
    # sound_tests()
    # arm_tests()
    # drive_color_tests()
    #     Color tests are [Black, Red, Brown, White]

def drive_proximity_tests():
    robot = rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(12,60)
    robot.drive_system.go_backward_until_distance_is_greater_than(18, 50)
    robot.drive_system.go_until_distance_is_within(13,1,40)

def drive_camera_tests():
    robot = rosebot.RoseBot()
    robot.drive_system.spin_clockwise_until_sees_object(50,40)
    robot.drive_system.display_camera_data()
    time.sleep(3)
    robot.drive_system.spin_counterclockwise_until_sees_object(50,40)
    robot.drive_system.display_camera_data()

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
main()