
import sys
import math
from sympy import Symbol

sys.path.append(r'/home/cmesado/Dropbox/dev')
sys.path.append(r'C:\Users\cmem\onedrive_cmem\OneDrive - ENUSA Industrias Avanzadas, S.A., S.M.E\python')

from physics.drivers.body import Body


def test_newton_i():
    """
    Relación 8 las fuerzas
    Problema 14
    """
    mu = Symbol('mu')
    alpha = math.radians(25)
    m = 250
    g = 9.81
    W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
    N = (0.0, m*g*math.sin(alpha))
    Fr = (-mu*m*g*math.cos(alpha), 0.0)

    body = Body(dimensions=2)

    body.set('mass', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    a = body.solve_newton_equation('a', axis='x')
    assert a

    f = m*a[0].subs('mu', 0.0)
    assert str(round(f, 2)) == '-1036.47'

    f = m*a[0].subs('mu', 0.1)
    assert str(round(f, 2)) == '-1258.74'

def test_newton_ii():
    """
    Relación 8 las fuerzas
    Problema 14
    """
    mu = 0.1
    alpha = math.radians(25)
    m = 250
    g = 9.81
    W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
    N = (0.0, m*g*math.sin(alpha))
    Fr = (-mu*m*g*math.cos(alpha), 0.0)

    body = Body(dimensions=2)

    body.set('mass', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    a = body.solve_newton_equation('a', axis='x')
    assert a

    f = m*a[0]
    assert str(round(f, 2)) == '-1258.74'


# body1 = Body()
# body1.apply_force((100, 100))

# body2 = Body()
# body2.apply_force((100, 100))

