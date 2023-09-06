
import sys
import math

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.body import Body
from physics.drivers.universe import Universe
from physics.utils import compare_floats, magnitude


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

    body = Body('A', dimensions=2)

    body.set('gravity', g)
    body.set('initial_position', p0)
    body.set('initial_velocity', v0)
    body.set('position', y, axis='y')

    universe = Universe()
    universe.add_body(body)

    t = universe.solve_linear_position_equation('A', 't', axis='y')
    
    assert compare_floats(t[0], 0.0)
    assert compare_floats(t[1], 3.20)

    body.set('time', t[1])

    p_x = universe.solve_linear_position_equation('A', 'p', axis='x', first_positive_root=True)
    
    assert compare_floats(p_x, 50.33)

def test_mrua_2d_ii():
    """
    Tema 0: Vectores, cinemática
    Problema 10
    """
    alpha = math.radians(-30)
    g = (0.0, -9.81)
    p0 = (0.0, 10.0)
    v0 = (2.0*math.cos(alpha), 2.0*math.sin(alpha))
    py = 0.0

    body = Body('A', dimensions=2)

    body.set('gravity', g)
    body.set('initial_position', p0)
    body.set('initial_velocity', v0)
    body.set('position', py, axis='y')

    universe = Universe()
    universe.add_body(body)

    t = universe.solve_linear_position_equation('A', 't', axis='y', first_positive_root=True)
    
    assert compare_floats(t, 1.33)

    body.set('time', t)

    p_x = universe.solve_linear_position_equation('A', 'p', axis='x', first_positive_root=True)
    
    assert compare_floats(p_x, 2.30)

    v_x, v_y = universe.solve_linear_velocity_equation('A', 'v')
    
    assert compare_floats(v_x[0], 1.73)
    assert compare_floats(v_y[0], -14.04)

    v = magnitude((v[0][0], v[1][0]))

    assert compare_floats(v, 14.15)
