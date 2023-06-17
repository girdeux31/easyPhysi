
import math

none_type = type(None)


def magnitude(array):

    return math.sqrt(sum([x**2 for x in array]))
