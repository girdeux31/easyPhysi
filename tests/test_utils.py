import sys

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.utils import compare_floats, magnitude, distance, inner_product, angle


def test_compare_floats_small():

    assert compare_floats(1, 1.01)
    assert not compare_floats(1, 1.011)
    assert not compare_floats(1, 0.981)
    assert compare_floats(3.14, 3.1416)
    assert compare_floats(3.14E-10, 3.1416E-10)
    assert compare_floats(3.14E-10, 3.15E-10)
    assert not compare_floats(3.14E-10, 3.151E-10)

def test_compare_floats_big():

    assert compare_floats(1E+2, 1.01E+2)
    assert not compare_floats(1E+2, 1.011E+2)
    assert not compare_floats(1E+2, 0.981E+2)
    assert compare_floats(3.14E+2, 3.1416E+2)
    assert compare_floats(3.14E+10, 3.1416E+10)
    assert compare_floats(3.14E+10, 3.15E+10)
    assert not compare_floats(3.14E+10, 3.151E+10)

def test_magnitude():

    u = (3, 4)
    assert magnitude(u) == 5.0

    v = (3.1416, 4.1234)
    assert compare_floats(magnitude(v), 5.18383, decimals=4)

def test_distance():

    u = (223.2, 34)
    v = (45, 3.1)

    assert compare_floats(distance(u, v), 180.8592, decimals=4)

def test_inner_product():

    u = (2, -3)
    v = (5, 1)

    assert compare_floats(inner_product(u, v), 7)

def test_angle():

    u = (2, 1, -2)
    v = (1, 1, 1)

    assert compare_floats(angle(u, v), 1.37)
