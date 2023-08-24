
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
    # TODO review methodology
    body_b = Body(name='B')
    body_b.set('mass', 5)
    body_b.set('position', (2, -2))

    body_bp = Body(name='Bp')
    body_bp.set('mass', 5)
    body_bp.set('position', (2, 0))

    field = Field()
    field.add_body(body_b)
    field.add_body(body_bp)

    Ep_b_solve = field.solve_gravitational_potential_energy_equation('B', 'Epg')
    Ep_bp_solve = field.solve_gravitational_potential_energy_equation('Bp', 'Epg')
    Ep_b_get = field.get_gravitational_potential_energy_over('B')
    Ep_bp_get = field.get_gravitational_potential_energy_over('Bp')

    assert compare_floats(Ep_b_solve[0]-Ep_bp_solve[0], 1.47E-10)
    assert compare_floats(Ep_b_get-Ep_bp_get, 1.47E-10)