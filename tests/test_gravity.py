
import sys

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.body import Body
from physics.drivers.field import Field
from physics.utils import compare_floats


def test_gravity_b1_2019_junio():
    """
    F2-PAU-Gravitation
    B1 2019 junio
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

    Fg_solve = field.solve_gravitation_equation('A', 'Fg')
    Fg_get = field.get_gravitational_force_over('A')

    assert str(round(Fg_solve[0]*1E+10, 2)) == '-1.25'
    assert str(round(Fg_get*1E+10, 2)) == '-1.25'
    assert compare_floats(Fg_get, -1.25E-10)