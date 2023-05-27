
import sys
import math

sys.path.append(r'/home/cmesado/Dropbox/dev')
sys.path.append(r'C:\Users\cmem\onedrive_cmem\OneDrive - ENUSA Industrias Avanzadas, S.A., S.M.E\python')

from physics.drivers.body import Body
from physics.utils import magnitude


def test_mrua_2d_i():
    """
    12 problemas movimientos 1d y 2d
    Problema 3
    """
    alpha = math.radians(45)
    g = (0.0, -9.81)
    p0 = (0.0, 0.0)
    v0 = (22.22*math.cos(alpha), 22.22*math.sin(alpha))
    y = 0.0

    body = Body(dimensions=2)

    body.set('gravity', g)
    body.set('initial_position', p0)
    body.set('initial_velocity', v0)
    body.set('position', y, axis='y')

    t = body.solve_position_equation('t', axis='y')
    assert t
    assert str(round(t[0], 1)) == '0.0'
    assert str(round(t[1], 2)) == '3.20'

    body.set('time', t[1])
    x = body.solve_position_equation('p', axis='x')
    assert x
    assert str(round(x[0], 2)) == '50.33'

def test_mrua_2d_ii():
    """
    Tema 0: Vectores, cinemática
    Problema 10
    """
    alpha = math.radians(-30)
    g = (0.0, -9.81)
    p0 = (0.0, 10.0)
    v0 = (2.0*math.cos(alpha), 2.0*math.sin(alpha))
    y = 0.0

    body = Body(dimensions=2)

    body.set('gravity', g)
    body.set('initial_position', p0)
    body.set('initial_velocity', v0)
    body.set('position', y, axis='y')

    t = body.solve_position_equation('t', axis='y')
    assert t
    assert str(round(t[0], 2)) == '-1.53'
    assert str(round(t[1], 2)) == '1.33'

    body.set('time', t[1])
    x = body.solve_position_equation('p', axis='x')
    assert x
    assert str(round(x[0], 2)) == '2.30'

    vx = body.solve_velocity_equation('v', axis='x')
    assert vx
    assert str(round(vx[0], 2)) == '1.73'

    vy = body.solve_velocity_equation('v', axis='y')
    assert vy
    assert str(round(vy[0], 2)) == '-14.04'

    v = magnitude((vx[0], vy[0]))
    assert str(round(v, 2)) == '14.15'
