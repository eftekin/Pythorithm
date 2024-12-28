# Create a function that takes the height and radius of a cone as arguments and returns
# the volume of the cone rounded to the nearest hundredth. See the resources tab for
# the formula.
# Examples
# cone_volume(3, 2) ➞ 12.57
# cone_volume(15, 6) ➞ 565.49
# cone_volume(18, 0) ➞ 0

import math


def cone_volume(h, r):
    if r == 0:
        return 0
    volume = (1 / 3) * math.pi * r**2 * h
    return round(volume, 2)


# test cases
print(cone_volume(3, 2))
print(cone_volume(15, 6))
print(cone_volume(18, 0))
