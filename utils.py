import math
from scipy.constants import physical_constants as pyc

none_type = type(None)

epsilon_0 = pyc['vacuum electric permittivity'][0]
K = 1/4/math.pi/epsilon_0


def magnitude(array):

    return math.sqrt(sum([x**2 for x in array]))

def distance(array_u, array_v):

    if len(array_u) != len(array_v):
        raise ValueError('Lengths of arrays mismatch')

    # to use expression with sympy you must not use math.sqrt
    return sum([(u-v)**2 for u, v in zip(array_u, array_v)])**0.5

def inner_product(array_u, array_v):

    if len(array_u) != len(array_v):
        raise ValueError('Lengths of arrays mismatch')

    return sum([u*v for u, v in zip(array_u, array_v)])

def angle(array_u, array_v):

    if len(array_u) != len(array_v):
        raise ValueError('Lengths of arrays mismatch')
    
    return math.acos(inner_product(array_u, array_v)/magnitude(array_u)/magnitude(array_v))

def angle_with_horizontal(point_a, point_b):

    if len(point_a) != len(point_b):
        raise ValueError('Lengths of points mismatch')

    point_c = tuple([b-a for a, b in zip(point_a, point_b)])

    return math.atan2(point_c[1], point_c[0])

def compare_floats(float_ref, float_test, decimals=2):
    
    if not hasattr(float_ref, '__float__') or not hasattr(float_test, '__float__'):
        raise ValueError('Arguments \'float_ref\' and \'float_test\' must be convertible to floats')

    power = round(math.log10(abs(float_ref))) if float_ref != 0.0 else 0.0
    power = power - decimals
    eps = 10**(power)

    return True if float_test - eps <= float_ref <= float_test + eps else False
    