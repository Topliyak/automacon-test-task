import math


WHEEL_DISTANCE = 1290 / 1000 # wheel base = 1290 millimeters
WHEEL_RADIUS = 250 / 2000 # diameter = 250 millimeters
WHEEL_LENGTH = 2 * math.pi * WHEEL_RADIUS


def get_wheel_angle_rad_and_frequency(robot_linear_vel_x: float, robot_angular_vel_z: float) -> tuple[float, float]:
    """ Convert linear velocity x axis projection and angular velocity 
        to pair wheel angle (radians) and wheel frequency (turns per second) """
    
    if math.isclose(robot_linear_vel_x, 0) and math.isclose(robot_angular_vel_z, 0):
        return 0, 0
    
    if math.isclose(robot_linear_vel_x, 0):
        freq = abs(robot_angular_vel_z) * WHEEL_DISTANCE / WHEEL_LENGTH

        wheel_angle_rad = math.pi * 0.5
        if robot_angular_vel_z > 0:
            wheel_angle_rad = math.pi * 1.5

        return wheel_angle_rad, freq

    if math.isclose(robot_angular_vel_z, 0):
        freq = abs(robot_linear_vel_x) / WHEEL_LENGTH

        wheel_angle_rad = 0
        if robot_linear_vel_x < 0:
            wheel_angle_rad = math.pi

        return wheel_angle_rad, freq

    angle_rad = math.atan(abs(robot_angular_vel_z) * WHEEL_DISTANCE / abs(robot_linear_vel_x))

    linear_vel = abs(robot_linear_vel_x) / math.cos(angle_rad)
    freq = linear_vel / WHEEL_LENGTH

    if robot_linear_vel_x < 0:
        if robot_angular_vel_z > 0:
            wheel_angle_rad = math.pi + angle_rad
        else:
            wheel_angle_rad = math.pi - angle_rad
    else:
        if robot_angular_vel_z > 0:
            wheel_angle_rad = 2 * math.pi - angle_rad
        else:
            wheel_angle_rad = angle_rad

    return wheel_angle_rad, freq
