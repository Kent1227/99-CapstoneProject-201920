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

    # Teleoperation functions

    def forward(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), int(rspeed))

    def backward(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), int(rspeed))

    def left(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), int(rspeed))

    def right(self, lspeed, rspeed):
        self.robot.drive_system.go(int(lspeed), int(rspeed))

    def stop(self):
        self.stop()

    # Arm and Claw functions

    def raise_arm(self):
        self.raise_arm()

    def lower_arm(self):
        self.lower_arm()

    def calibrate_arm(self):
        self.calibrate_arm()

    def move_arm_to_position(self, desired_position):
        self.move_arm_to_position(desired_position)

    # Control

    def quit(self):
        self.quit()

    def exit(self):
        self.exit()

    # Drive system

    def stright_for_seconds(self, seconds):


    # Sound
