
import sys

sys.path.append(r'/home/cmesado/Dropbox/dev/pyphysics')

from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.utils import compare_floats, magnitude


def test_gravity_b1_2019_junio_a():
    """
    F2-PAU-Gravitation
    B1.a 2019 junio
    """
    body_a = Body('A')
    body_a.set('mass', 3)
    body_a.set('position', (0, 0))

    body_b = Body('B')
    body_b.set('mass', 5)
    body_b.set('position', (2, -2))

    universe = Universe()
    universe.add_body(body_a)
    universe.add_body(body_b)

    Fg_x, Fg_y = universe.gravitational_force_equation('B').solve(['Fg_x', 'Fg_y'])
    Fg = magnitude((Fg_x, Fg_y))  # always positive value

    assert compare_floats(Fg_x, -8.84E-11)
    assert compare_floats(Fg_y, +8.84E-11)
    assert compare_floats(Fg, +1.25E-10)

def test_gravity_b1_2019_junio_b():
    """
    F2-PAU-Gravitation
    B1.b 2019 junio
    """
    pa = (0, 0)
    pb_0 = (2, -2)
    pb_1 = (2, 0)

    body_a = Body('A')
    body_a.set('mass', 3)
    body_a.set('position', pa)

    body_b = Body('B')
    body_b.set('mass', 5)

    universe = Universe()
    universe.add_body(body_a)
    universe.add_body(body_b)

    body_b.set('position', pb_0)

    Ep_0 = universe.gravitational_potential_energy_equation('B').solve('Ug')

    body_b.set('position', pb_1)
    
    Ep_1 = universe.gravitational_potential_energy_equation('B').solve('Ug')

    W = Ep_0[0] - Ep_1[0] # W = -AEp = Ep_0 - Ep_1

    assert compare_floats(W, 1.47E-10)

def test_gravity_a1_2019_junio_a1():
    """
    F2-PAU-Gravitation
    A1.a1 2019 junio
    """
    body_a = Body('A')
    body_a.set('mass', 5)
    body_a.set('position', (4, 3))
    point = (0, 0)

    universe = Universe()
    universe.add_body(body_a)

    g_x, g_y = universe.gravitational_field_intensity_equation(point).solve(['gg_x', 'gg_y'])
    g = magnitude((g_x, g_y))  # always positive value
    
    assert compare_floats(g_x, +1.06E-11)
    assert compare_floats(g_y, +7.99E-12)
    assert compare_floats(g, +1.33E-11)

