
import sys
import math

sys.path.append(r'/home/cmesado/Dropbox/dev/pyphysics')

from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.utils import compare_floats, magnitude


def test_mrua_3():
    """
    URL: https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/12._problemas_movimientos_en_una_y_dos_dimensiones.pdf
    Problem: 3
    Statement: A midfielder tries to surprise a goalkeeper who is advanced from 50 m away by hitting the ball in the right direction. The ball leaves his boot at 80 km/h and at an angle of 45º from the ground. The goalkeeper is 7 m away from his goal and takes 1 second to react and move back at a speed of 2 m/s. Will it be a goal or not?"
    """
    alpha = math.radians(45)
    g = (0.0, -9.81)
    p0 = (0.0, 0.0)
    v0 = (22.22*math.cos(alpha), 22.22*math.sin(alpha))
    y = 0.0

    body = Body('body', dimensions=2)

    body.set('g', g)
    body.set('p0', p0)
    body.set('v0', v0)
    body.set('p_y', y)

    universe = Universe()
    universe.add_body(body)

    t = universe.linear_position_equation('body').get_equation('y').solve('t', first_positive_root=True)
    
    assert compare_floats(t, 3.20)

    body.set('t', t)

    p_x = universe.linear_position_equation('body').get_equation('x').solve('p_x', first_positive_root=True)
    
    assert compare_floats(p_x, 50.33)

def test_mrua_10():
    """
    URL: https://fq.iespm.es/documentos/janavarro/fisica2bach/T0_vectores_cinematica.pdf
    Problem: 10
    Statement: A ball falls from a roof located 10 m high, forming a 30º angle with the horizontal, with a speed of 2 m/s. Calculate:
    a) At what distance from the wall does it hit the ground?
    b) The speed it has when it reaches the ground (disregard air friction).
    """
    alpha = math.radians(-30)
    g = (0.0, -9.81)
    p0 = (0.0, 10.0)
    v0 = (2.0*math.cos(alpha), 2.0*math.sin(alpha))
    py = 0.0

    body = Body('body', dimensions=2)

    body.set('g', g)
    body.set('p0', p0)
    body.set('v0', v0)
    body.set('p_y', py)

    universe = Universe()
    universe.add_body(body)

    t = universe.linear_position_equation('body').get_equation('y').solve('t', first_positive_root=True)
    
    assert compare_floats(t, 1.33)

    body.set('t', t)

    p_x = universe.linear_position_equation('body').get_equation('x').solve('p_x', first_positive_root=True)
    
    assert compare_floats(p_x, 2.30)

    v_x, v_y = universe.linear_velocity_equation('body').solve(['v_x', 'v_y'])
    v = magnitude((v_x, v_y))
    
    assert compare_floats(v_x, 1.73)
    assert compare_floats(v_y, -14.04)
    assert compare_floats(v, 14.15)
