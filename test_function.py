import math

import pytest

import core


@pytest.mark.parametrize('linear_x,angular_z,expected_angle,expected_frequency', [
    (0, 0, 0, 0),
    (1.6, 0, 0, 1.6 / core.WHEEL_LENGTH),
    (-1, 0, math.pi, 1 / core.WHEEL_LENGTH),
    (0, 1, 1.5 * math.pi, 1.6424790127),
    (0, -1, 0.5 * math.pi, 1.6424790127),
    (1.6, -1, 0.678540316, 2.61684026818),
    (-1.6, 1, 3.8201329696, 2.61684026818),
    (1.6, 1, 5.6046449911, 2.61684026818),
    (-1.6, 1, 3.8201329696, 2.61684026818),
])
def test_function(linear_x, angular_z, expected_angle, expected_frequency):
    angle, freq = core.get_wheel_angle_rad_and_frequency(linear_x, angular_z)
    assert math.isclose(angle, expected_angle), f'Expected angle {expected_angle}, got {angle}'
    assert math.isclose(freq, expected_frequency), f'Expected frequency {expected_frequency}, got {freq}'
