
import os
import sys
import math
from sympy import Symbol

sys.path.append(r'/home/cmesado/Dropbox/dev/pyphysics')

from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe


def test_equation_i():
    """
    """
    file = './tests/ref/a_f_mu.png'

    mu = Symbol('mu')
    alpha = math.radians(25)
    m = 250
    g = 9.81
    W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
    N = (0.0, m*g*math.sin(alpha))
    Fr = (-mu*m*g*math.cos(alpha), 0.0)

    body = Body('body', dimensions=2)

    body.set('mass', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    universe = Universe()
    universe.add_body(body)

    if os.path.exists(file):
        os.remove(file)

    universe.newton_equation('body')['x'].plot('a_x', 'mu', [0, 1], points=200, path=file, show=False)

    assert os.path.exists(file)
