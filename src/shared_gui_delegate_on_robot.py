"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Kent Smith, Eddie Mannan, Cleo Barmes, and Ethan Mahn.
  Winter term, 2018-2019.
"""

import m4_extra as m4
import m3_extra as m3
import m2_Extra as m2
import m1_extra as m1


class DelegateThatReceives(object):
    def __init__(self, robot, mqtt_reciever = None):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot
        self.mqtt_reciever = mqtt_reciever
        self.leave = False

    # Teleoperation functions

    def forward(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), int(rspeed))

    def backward(self, lspeed, rspeed):
        self.robot.drive_system.go(-int(lspeed), -int(rspeed))

    def left(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), -int(rspeed))

    def right(self, lspeed, rspeed):
        self.robot.drive_system.go(-int(lspeed), int(rspeed))

    def stop(self):
        self.robot.drive_system.stop()

    # Arm and Claw functions

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, desired_position):
        self.robot.arm_and_claw.move_arm_to_position(desired_position)

    # Control

    def quit(self):
        self.leave = True

    # Drive system

    def go_straight_for_seconds(self, seconds, speed):
        self.robot.drive_system.go_straight_for_seconds(seconds, speed)

    def go_straight_for_inches_using_time(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches, speed)

    # Sound

    def beep_number_of_times(self, number_of_beeps):
        self.robot.sound_system.beep_number_of_times(number_of_beeps)

    def play_tone(self, duration, frequency):
        self.robot.sound_system.play_tone(duration, frequency)

    def speak(self, given_phrase):
        self.robot.sound_system.speak(given_phrase)

    # Proximity Sensor
    def use_proximity_to_move_forward(self, range, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(range, speed)

    def use_proximity_to_move_backward(self, range, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(range), int(speed))

    def use_proximity_to_move_exact_range(self, range, delta, speed):
        self.robot.drive_system.go_until_distance_is_within(delta, range, speed)

    # Color Sensor
    def intensity_greater(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(intensity, speed)

    def intensity_lesser(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(intensity, speed)

    def color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(color, speed)

    def color_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, speed)

    # Camera
    def camera_cw(self,area,speed):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed),int(area))

    def camera_ccw(self,area,speed):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed),int(area))

    def camera_data(self):
        self.robot.drive_system.display_camera_data()

    # Later additions
    def calibrate_true(self):
        self.robot.drive_system.calibrate_true()

    def go_true(self, inches):
        print("go true", inches)
        self.robot.drive_system.go_true(inches)

    def turn(self,degrees):
        print("turn", degrees)
        self.robot.drive_system.turn_degrees(degrees)

    # m3 Beep_Proximity
    def m3_beep_proximity(self, initial, delta, speed):
        m3.m3_beep_proximity(int(initial), float(delta), int(speed))

    def m3_beep_retrieve(self, dir, speed):
        m3.m3_beep_retrieve(dir, int(speed))

    #m3 Sprint 3
    def m3_baby_robot(self, speed, progress_state):
        m3.m3_baby_walk(int(speed), int(progress_state), self.robot, self.mqtt_reciever)

    def sleep_time(self):
        m3.sleep_time()

    # m4
    def m4_led_proximity(self, initial, delta, speed):
        m4.m4_led_proximity(int(initial), float(delta), int(speed))

    def m4_led_retrieve(self, dir, speed):
        m4.m4_led_retrieve(dir, speed)

    # m2 stuff
    def m2_find_homework(self):
        m2.find_homework(self.robot)

    def m2_find_games(self):
        m2.find_games(self.robot)

    def m2_find_food(self):
        m2.find_food(self.robot)

    def m2_go_to_sleep(self):
        m2.go_to_sleep(self.robot)

    # m1

    def m1_disco(self):
        m1.disco(self.robot)

    def m1_raise(self):
        m1.raise_the_roof(self.robot)

    def m1_shake(self):
        m1.shake(self.robot)

    def m1_spin(self):
        m1.spin(self.robot)

    # def m2_beep_proxy(self, initial, delta, speed):
    # m2.beep_proxy(self.robot, int(initial), float(delta), int(speed))

    # def m2_beep_retrieve(self, dir, speed):
    # m2.beep_retrieve(self.robot, dir, int(speed))

    # m4 sprint 3: Chess
    def retrieve_piece(self, commands):
        m4.chess_commands(commands)
        m4.pick_up()
    def place_piece(self, commands):
        m4.chess_commands(commands)
        m4.put_down()
    def dispose_piece(self, commands):
        m4.chess_commands(commands)
        m4.dispose()

    def lost(self):
        m4.robot_lost()
    def locate(self):
        m4.locate_robot()
    def read_intensity(self):
        print(self.robot.sensor_system.color_sensor.get_reflected_light_intensity())