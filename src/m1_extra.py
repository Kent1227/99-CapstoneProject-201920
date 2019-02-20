import rosebot
import time


def disco(robot):
    """
    :type robot: rosebot.RoseBot
    """
    robot.drive_system.pivot_left(50, 2)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_right(50, 2)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.pivot_left(50, 2)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_right(50, 2)
    robot.arm_and_claw.lower_arm()


def shake(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    robot.drive_system.spin_clockwise_until_sees_object(100, 1)
    robot.drive_system.spin_counterclockwise_until_sees_object(100, 1)
    robot.drive_system.spin_clockwise_until_sees_object(100, 1)
    robot.drive_system.spin_counterclockwise_until_sees_object(100, 1)
    robot.drive_system.spin_clockwise_until_sees_object(100, 1)
    robot.drive_system.spin_counterclockwise_until_sees_object(100, 1)
    robot.drive_system.spin_clockwise_until_sees_object(100, 1)
    robot.drive_system.spin_counterclockwise_until_sees_object(100, 1)
    robot.drive_system.spin_clockwise_until_sees_object(100, 1)
    robot.drive_system.spin_counterclockwise_until_sees_object(100, 1)
    robot.drive_system.spin_clockwise_until_sees_object(100, 1)
    robot.drive_system.spin_counterclockwise_until_sees_object(100, 1)


def spin(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    robot.drive_system.spin_clockwise_until_sees_object(100, 1000000000)


def raise_the_roof(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    robot.arm_and_claw.calibrate_arm()
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.lower_arm()
