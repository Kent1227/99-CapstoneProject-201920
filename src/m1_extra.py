import rosebot


def disco(robot):
    """
    :type robot: rosebot.RoseBot
    """
    while True:
        robot.drive_system.go(100, 100)
        if robot.sensor_system.ir_proximity_sensor.get_distance() < 5:
            break
        if robot.sensor_system.color_sensor.get_color_as_name() is "red":
            break
    robot.drive_system.pivot_left(50, 2)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_right(50, 2)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.pivot_left(50, 2)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.pivot_right(50, 2)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.stop()


def shake(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    while True:
        robot.drive_system.go(100, 100)
        if robot.sensor_system.ir_proximity_sensor.get_distance() < 5:
            break
        if robot.sensor_system.color_sensor.get_color_as_name() is "red":
            break
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
    robot.drive_system.stop()


def spin(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    while True:
        robot.drive_system.go(100, 100)
        if robot.sensor_system.ir_proximity_sensor.get_distance() < 5:
            break
        if robot.sensor_system.color_sensor.get_color_as_name() is "red":
            break
    robot.drive_system.spin_clockwise_until_sees_object(100, 1000000000)
    robot.drive_system.stop()


def raise_the_roof(robot):
    """
    :type robot: rosebot.RoseBot
    :param robot:
    :return:
    """
    while True:
        robot.drive_system.go(100, 100)
        if robot.sensor_system.ir_proximity_sensor.get_distance() < 5:
            break
        if robot.sensor_system.color_sensor.get_color_as_name() is "red":
            break
    robot.arm_and_claw.calibrate_arm()
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.lower_arm()
    robot.drive_system.stop()
