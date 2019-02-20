import rosebot


def disco(robot):
    """
    :type robot: rosebot.RoseBot
    """
    robot.drive_system.go_forward_until_distance_is_less_than(10, 100)
    robot.drive_system.pivot_left(50, 1)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_right(50, 1)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.stop()


def shake(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    robot.drive_system.go_forward_until_distance_is_less_than(10, 100)
    robot.drive_system.turn_degrees(40, 100)
    robot.drive_system.turn_degrees(-40, 100)
    robot.drive_system.turn_degrees(40, 100)
    robot.drive_system.turn_degrees(-40, 100)
    robot.drive_system.turn_degrees(40, 100)
    robot.drive_system.turn_degrees(-40, 100)
    robot.drive_system.turn_degrees(40, 100)
    robot.drive_system.turn_degrees(-40, 100)
    robot.drive_system.stop()


def spin(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    robot.drive_system.go_forward_until_distance_is_less_than(10, 100)
    robot.drive_system.turn_degrees(720, 100)
    robot.drive_system.stop()


def raise_the_roof(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    robot.drive_system.go_forward_until_distance_is_less_than(10, 100)
    robot.arm_and_claw.calibrate_arm()
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.lower_arm()
    robot.drive_system.stop()
