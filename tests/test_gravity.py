
import sys

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.body import Body
from physics.drivers.field import Field
from physics.utils import compare_floats


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

    field = Field()
    field.add_body(body_a)
    field.add_body(body_b)

    Fg_solve = field.solve_gravitational_force_equation('A', 'Fg')
    Fg_get = field.get_gravitational_force_over('A')

    assert compare_floats(Fg_solve[0], -1.25E-10)
    assert compare_floats(Fg_get, -1.25E-10)

def test_gravity_b1_2019_junio_b():
    """
    F2-PAU-Gravitation
    B1.b 2019 junio
    """
    body_b = Body(name='B')
    body_b.set('mass', 5)
    body_b.set('position', (2, -2))

    field = Field()
    field.add_body(body_b)

    Ep_b_solve = field.solve_gravitational_potential_energy_equation('B', 'Ug')
    Ep_b_get = field.get_gravitational_potential_energy_over('B')

    body_b.set('position', (2, 0))
    
    Ep_bp_solve = field.solve_gravitational_potential_energy_equation('B', 'Ug')
    Ep_bp_get = field.get_gravitational_potential_energy_over('B')

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

    field = Field()
    field.add_body(body_a)

    g_solve = field.solve_gravitational_field_intensity_equation(point, 'gg')
    g_get = field.get_gravitational_field_intensity_in(point)
    
    assert compare_floats(g_solve[0], -1.33E-11)
    assert compare_floats(g_get, -1.33E-11)

def test_gravity_b1_2022_model_b():
    """
    F2-PAU-Gravitation
    B1.b 2022 model
    """
    ma = 1
    mb = 10
    g = -9.81
    pb = (0, 0)
    pa_x = 0

    body_a = Body(name='A')
    body_a.set('mass', ma)
    body_a.set('position', pa_x, axis='x')
    body_a.set('gravitational_force', ma*g*1E-9)

    body_b = Body(name='B')
    body_b.set('mass', mb)
    body_b.set('position', pb)

    field = Field()
    field.add_body(body_a)
    field.add_body(body_b)

    p_solve = field.solve_gravitational_force_equation('A', 'p')

    assert compare_floats(p_solve[1], 0.26)