
import sys

sys.path.append(r'/home/cmesado/Dropbox/dev/easyPhysi')

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.utils import compare_floats, magnitude


def test_gravity_b1a_2019_junio_coincidentes():
    """
    URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf
    Problem: B1.a 2019 junio
    Statement: A point mass A, MA = 3 kg, is located on the xy-plane, at the origin of coordinates. If a point mass B, MB = 5 kg, is placed at point (2, -2) m, determine:
    a) The force exerted by mass A on mass B.
    """
    body_a = Body('A')
    body_a.set('m', 3)
    body_a.set('p', (0, 0))

    body_b = Body('B')
    body_b.set('m', 5)
    body_b.set('p', (2, -2))

    universe = Universe()
    universe.add_body(body_a)
    universe.add_body(body_b)

    Fg_x, Fg_y = universe.gravitational_force_equation('B').solve(['Fg_x', 'Fg_y'])
    Fg = magnitude((Fg_x, Fg_y))  # always positive value

    assert compare_floats(Fg_x, -8.84E-11)
    assert compare_floats(Fg_y, +8.84E-11)
    assert compare_floats(Fg, +1.25E-10)

def test_gravity_b1a_2019_junio_coincidentes_3d():
    """
    URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf
    Problem: B1.a 2019 junio
    Statement: A point mass A, MA = 3 kg, is located on the xy-plane, at the origin of coordinates. If a point mass B, MB = 5 kg, is placed at point (2, -2, 0) m, determine:
    a) The force exerted by mass A on mass B.
    """
    body_a = Body('A', dimensions=3)
    body_a.set('m', 3)
    body_a.set('p', (0, 0, 0))

    body_b = Body('B', dimensions=3)
    body_b.set('m', 5)
    body_b.set('p', (2, -2, 0))

    universe = Universe(dimensions=3)
    universe.add_body(body_a)
    universe.add_body(body_b)

    Fg_x, Fg_y, Fg_z = universe.gravitational_force_equation('B').solve(['Fg_x', 'Fg_y', 'Fg_z'])
    Fg = magnitude((Fg_x, Fg_y, Fg_z))  # always positive value

    assert compare_floats(Fg_x, -8.84E-11)
    assert compare_floats(Fg_y, +8.84E-11)
    assert compare_floats(Fg_z, 0.0)
    assert compare_floats(Fg, +1.25E-10)

def test_gravity_b1b_2019_junio_coincidentes():
    """
    URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf
    Problem: B1.b 2019 junio
    Statement: The work required to move mass B from point (2, -2) m to point (2, 0) m due to the gravitational field created by mass A.
    """
    pa = (0, 0)
    pb_0 = (2, -2)
    pb_1 = (2, 0)

    body_a = Body('A')
    body_a.set('m', 3)
    body_a.set('p', pa)

    body_b = Body('B')
    body_b.set('m', 5)

    universe = Universe()
    universe.add_body(body_a)
    universe.add_body(body_b)

    body_b.set('p', pb_0)

    Ug_0 = universe.gravitational_potential_energy_equation('B').solve('Ug')

    body_b.set('p', pb_1)
    
    Ug_1 = universe.gravitational_potential_energy_equation('B').solve('Ug')

    W = Ug_0[0] - Ug_1[0] # W = -AEp = Ug_0 - Ug_1

    assert compare_floats(W, 1.47E-10)

def test_gravity_a1a_2019_junio():
    """
    URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf
    Problem: A1.a 2019 junio
    Statement: A point mass m1 = 5 kg is located at the point (4, 3) m.
    a) Determine the intensity of the gravitational field created by mass m1 at the origin of coordinates.
    """
    body_a = Body('A')
    body_a.set('m', 5)
    body_a.set('p', (4, 3))
    point = (0, 0)

    universe = Universe()
    universe.add_body(body_a)

    g_x, g_y = universe.gravitational_field_intensity_equation(point).solve(['gg_x', 'gg_y'])
    g = magnitude((g_x, g_y))  # always positive value
    
    assert compare_floats(g_x, +1.06E-11)
    assert compare_floats(g_y, +7.99E-12)
    assert compare_floats(g, +1.33E-11)

