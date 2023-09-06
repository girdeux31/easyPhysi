
import sys

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.body import Body
from physics.drivers.universe import Universe
from physics.utils import compare_floats, magnitude


def test_gravity_b1_2019_junio_a():
    """
    F2-PAU-Gravitation
    B1.a 2019 junio
    """
    body_a = Body(name='A')
    body_a.set('mass', 3)
    body_a.set('position', (0, 0))

    body_b = Body(name='B')
    body_b.set('mass', 5)
    body_b.set('position', (2, -2))

    universe = Universe()
    universe.add_body(body_a)
    universe.add_body(body_b)

    Fg_solve_x = universe.solve_gravitational_force_equation('B', 'Fg', axis='x')
    Fg_solve_y = universe.solve_gravitational_force_equation('B', 'Fg', axis='y')
    Fg_solve = magnitude((Fg_solve_x[0], Fg_solve_y[0]))  # positive value always

    Fg_get_x = universe.get_gravitational_force_over('B', axis='x')
    Fg_get_y = universe.get_gravitational_force_over('B', axis='y')
    Fg_get = magnitude((Fg_get_x, Fg_get_y))  # positive value always

    assert compare_floats(Fg_solve_x[0], -8.84E-11)
    assert compare_floats(Fg_solve_y[0], +8.84E-11)
    assert compare_floats(Fg_solve, +1.25E-10)

    assert compare_floats(Fg_get_x, -8.84E-11)
    assert compare_floats(Fg_get_y, +8.84E-11)
    assert compare_floats(Fg_get, +1.25E-10)

def test_gravity_b1_2019_junio_b():
    """
    F2-PAU-Gravitation
    B1.b 2019 junio
    """
    body_b = Body(name='B')
    body_b.set('mass', 5)
    body_b.set('position', (2, -2))

    universe = Universe()
    universe.add_body(body_b)

    Ep_b_solve = universe.solve_gravitational_potential_energy_equation('B', 'Ug')
    Ep_b_get = universe.get_gravitational_potential_energy_over('B')

    body_b.set('position', (2, 0))
    
    Ep_bp_solve = universe.solve_gravitational_potential_energy_equation('B', 'Ug')
    Ep_bp_get = universe.get_gravitational_potential_energy_over('B')

    assert compare_floats(Ep_b_solve[0]-Ep_bp_solve[0], 1.47E-10)
    assert compare_floats(Ep_b_get-Ep_bp_get, 1.47E-10)

def test_gravity_a1_2019_junio_a1():
    """
    F2-PAU-Gravitation
    A1.a1 2019 junio
    """
    body_a = Body(name='A')
    body_a.set('mass', 5)
    body_a.set('position', (4, 3))
    point = (0, 0)

    universe = Universe()
    universe.add_body(body_a)

    g_solve_x = universe.solve_gravitational_field_intensity_equation(point, 'gg', axis='x')
    g_solve_y = universe.solve_gravitational_field_intensity_equation(point, 'gg', axis='y')
    g_solve = magnitude((g_solve_x[0], g_solve_y[0]))  # positive value always

    g_get_x = universe.get_gravitational_field_intensity_in(point, axis='x')
    g_get_y = universe.get_gravitational_field_intensity_in(point, axis='y')
    g_get = magnitude((g_get_x, g_get_y))  # positive value always
    
    assert compare_floats(g_solve_x[0], +1.06E-11)
    assert compare_floats(g_solve_y[0], +7.99E-12)
    assert compare_floats(g_solve, +1.33E-11)

    assert compare_floats(g_get_x, +1.06E-11)
    assert compare_floats(g_get_y, +7.99E-12)
    assert compare_floats(g_get, +1.33E-11)
