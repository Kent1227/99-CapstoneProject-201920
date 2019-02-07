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
    while True: #must end to quit
        time.sleep(0.01)


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
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