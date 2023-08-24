import sys

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.tuple import Tuple

tup = Tuple('a', dimensions=3)

def test_item():

    assert len(tup) == 3
    assert tup[0].name == 'a'

def test_iter():

    for value in tup:
        assert value.name == 'a'

def test_define():

    tup.define((1, 2, 3))
    assert tup[2] == 3

    tup.define(99, 'z')
    assert tup[2] == 99

def test_undefine():

    tup.define((1, 2, 3))

    tup.undefine('z')
    assert hasattr(tup[2], 'name')

    tup.undefine()

    for value in tup:
        assert hasattr(value, 'name')
