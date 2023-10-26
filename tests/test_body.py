import os
import sys
from contextlib import redirect_stdout

sys.path.append(r'/home/cmesado/Dropbox/dev/pyphysics')

from pyphysics.drivers.body import Body


def test_body_2d():

    g = (0.0, -9.81)
    p = (0.0, 1.0)

    body = Body('A')

    body.set('g', g)
    body.set('p_x', p[0])
    body.set('p_y', p[1])
    body.help()

def test_body_3d():

    g = (0.0, 0.0, -9.81)
    p = (0.0, 1.0, 2.0)

    body = Body('A', dimensions=3)

    body.set('g', g)
    body.set('p_x', p[0])
    body.set('p_y', p[1])
    body.set('p_z', p[2])
    body.help()

def test_body_help():

    file = r'tests/ref/properties.txt'

    if os.path.exists(file):
        os.remove(file)

    with open(file, 'w') as f:
        with redirect_stdout(f):
    
            body = Body('A')
            body.help()

    assert os.path.exists(file)
