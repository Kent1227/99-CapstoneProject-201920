"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Kent Smith, Eddie Mannan, Cleo Barmes, and Ethan Mahn.
  Winter term, 2018-2019.
"""


class DelegateThatReceives(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot
        self.leave = False

    # Teleoperation functions

    def forward(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), int(rspeed))

    def backward(self, lspeed, rspeed):
        self.robot.drive_system.go(-int(lspeed), -int(rspeed))

    def left(self, lspeed, rspeed):
        self.robot.drive_system.go(-int(lspeed), int(rspeed))

    def right(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), -int(rspeed))

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
        self.robot.drive_system.go_straight_for_inches_using_time(inches, speed)

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
    def use_proximity_to_move_forward(self, range):
        self.go_forward_until_distance_is_less_than(range, speed)

    def use_proximity_to_move_backward(self, range):
        self.go_backward_until_distance_is_greater_than(range, speed)

    def use_proximity_to_move_exact_range(self, range, delta):
        self.go_until_distance_is_within(delta, range, speed)