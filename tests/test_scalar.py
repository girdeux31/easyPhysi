import sys

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.scalar import Scalar

scalar = Scalar('a')

def test_item():

    assert scalar.name == 'a'

def test_define():

    scalar.define(99)
    assert scalar.value == 99

def test_undefine():

    scalar.define(99)

    scalar.undefine()
    assert hasattr(scalar, 'name')

