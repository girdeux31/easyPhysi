import sys
import math

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.body import Body, electron
from physics.drivers.universe import Universe
from physics.utils import compare_floats, magnitude


def test_electrical_b1_2019_junio_a():
    """
    F4.1-PAU-Electric Field
    A3.a 2021 modelo
    """
    point = (4, 0)

    body_1 = Body('1')
    body_1.set('charge', 5E-9)
    body_1.set('position', (0, +3))

    body_2 = Body('2')
    body_2.set('charge', 5E-9)
    body_2.set('position', (0, -3))

    universe = Universe()
    universe.add_body(body_1)
    universe.add_body(body_2)

    Ee_x, Ee_y = universe.solve_electrical_field_intensity_equation(point, 'Ee')
    Ee = magnitude((Ee_x[0], Ee_y[0]))  # always positive value

    assert compare_floats(Ee_x[0], 2.88)  # TODO switch
    assert compare_floats(Ee_y[0], 0.0)
    assert compare_floats(Ee, 2.88)

    Ee_x, Ee_y = universe.get_electrical_field_intensity_in(point)
    Ee = magnitude((Ee_x[0], Ee_y[0]))  # always positive value

    assert compare_floats(Ee_x[0], 2.88)
    assert compare_floats(Ee_y[0], 0.0)
    assert compare_floats(Ee, 2.88)

def test_electrical_b1_2019_junio_b():
    """
    F4.1-PAU-Electric Field
    A3.b 2021 modelo
    """
    point_0 = (0, 0)
    point_1 = (4, 0)

    body_1 = Body('1')
    body_1.set('charge', 5E-9)
    body_1.set('position', (0, +3))

    body_2 = Body('2')
    body_2.set('charge', 5E-9)
    body_2.set('position', (0, -3))

    universe = Universe()
    universe.add_body(body_1)
    universe.add_body(body_2)

    Ve_0 = universe.solve_electrical_potential_equation(point_0, 'Ve')
    Ve_1 = universe.solve_electrical_potential_equation(point_1, 'Ve')

    assert compare_floats(Ve_0[0], 30)
    assert compare_floats(Ve_1[0], 18)

    Ve_0 = universe.get_electrical_potential_in(point_0)
    Ve_1 = universe.get_electrical_potential_in(point_1)

    assert compare_floats(Ve_0[0], 30)
    assert compare_floats(Ve_1[0], 18)

def test_electrical_AP3_2019_junio_a():
    """
    F4.1-PAU-Electric Field
    AP3.a 2019 junio coincidentes
    """
    point = (4, 0)

    body_1 = Body('1')
    body_1.set('charge', -3E-9)
    body_1.set('position', (0, +3))

    body_2 = Body('2')
    body_2.set('charge', -3E-9)
    body_2.set('position', (0, -3))

    universe = Universe()
    universe.add_body(body_1)
    universe.add_body(body_2)

    Ee_x, Ee_y = universe.solve_electrical_field_intensity_equation(point, 'Ee')
    Ee = magnitude((Ee_x[0], Ee_y[0]))  # always positive value

    assert compare_floats(Ee_x[0], -1.73)
    assert compare_floats(Ee_y[0], 0.0)
    assert compare_floats(Ee, 1.73)

    Ee_x, Ee_y = universe.get_electrical_field_intensity_in(point)
    Ee = magnitude((Ee_x[0], Ee_y[0]))  # always positive value

    assert compare_floats(Ee_x[0], -1.73)
    assert compare_floats(Ee_y[0], 0.0)
    assert compare_floats(Ee, 1.73)

def test_electrical_AP3_2019_junio_b():
    """
    F4.1-PAU-Electric Field
    AP3.b 2019 junio coincidentes
    """
    point_0 = (0, 0)
    point_1 = (4, 0)

    body_1 = Body('1')
    body_1.set('charge', -3E-9)
    body_1.set('position', (0, +3))

    body_2 = Body('2')
    body_2.set('charge', -3E-9)
    body_2.set('position', (0, -3))

    universe = Universe()
    universe.add_body(body_1)
    universe.add_body(body_2)

    Ve_0 = universe.solve_electrical_potential_equation(point_0, 'Ve')
    Ve_1 = universe.solve_electrical_potential_equation(point_1, 'Ve')

    assert compare_floats(Ve_0[0], -18)
    assert compare_floats(Ve_1[0], -10.8)

    Ve_0 = universe.get_electrical_potential_in(point_0)
    Ve_1 = universe.get_electrical_potential_in(point_1)

    assert compare_floats(Ve_0[0], -18)
    assert compare_floats(Ve_1[0], -10.8)

def test_electrical_A3_2021_junio_coincidentes_a():
    """
    F4.1-PAU-Electric Field
    A3.a 2021 junio coincidentes
    """
    point = (0, 0)

    body_1 = Body('1')
    body_1.set('charge', 5E-9)
    body_1.set('position', (-1, +1))

    body_2 = Body('2')
    body_2.set('charge', 5E-9)
    body_2.set('position', (+1, +1))

    body_3 = Body('3')
    body_3.set('charge', 3E-9)
    body_3.set('position', (+1, -1))

    body_4 = Body('4')
    body_4.set('charge', 3E-9)
    body_4.set('position', (-1, -1))

    universe = Universe()
    universe.add_body(body_1)
    universe.add_body(body_2)
    universe.add_body(body_3)
    universe.add_body(body_4)

    Ee_x, Ee_y = universe.solve_electrical_field_intensity_equation(point, 'Ee')
    Ee = magnitude((Ee_x[0], Ee_y[0]))  # always positive value

    assert compare_floats(0.0, Ee_x[0])
    assert compare_floats(-12.72, Ee_y[0])
    assert compare_floats(12.72, Ee)

    Ee_x, Ee_y = universe.get_electrical_field_intensity_in(point)
    Ee = magnitude((Ee_x[0], Ee_y[0]))  # always positive value

    assert compare_floats(0.0, Ee_x[0])
    assert compare_floats(-12.72, Ee_y[0])
    assert compare_floats(12.72, Ee)

def test_electrical_A3_2021_junio_coincidentes_b():
    """
    F4.1-PAU-Electric Field
    A3.b 2021 junio coincidentes
    """
    point_0 = (0, 0)
    point_1 = (0, 1)

    body_1 = Body('1')
    body_1.set('charge', 5E-9)
    body_1.set('position', (-1, +1))

    body_2 = Body('2')
    body_2.set('charge', 5E-9)
    body_2.set('position', (+1, +1))

    body_3 = Body('3')
    body_3.set('charge', 3E-9)
    body_3.set('position', (+1, -1))

    body_4 = Body('4')
    body_4.set('charge', 3E-9)
    body_4.set('position', (-1, -1))

    universe = Universe()
    universe.add_body(body_1)
    universe.add_body(body_2)
    universe.add_body(body_3)
    universe.add_body(body_4)
    universe.add_body(electron)

    W = universe.get_electrical_work_over('electron', point_0, point_1)

    assert compare_floats(1.97E-18, W)

def test_electrical_A3_2023_modelo_b():
    """
    F4.1-PAU-Electric Field
    A3.b 2023 modelo
    """
    point_0 = (0, 2, 0)
    point_1 = (3, 0, 0)

    sphere = Body('sphere', dimensions=3)
    sphere.set('charge', 22.62E-9)
    sphere.set('position', (0, 0, 0))

    point = Body('point', dimensions=3)
    point.set('charge', 1E-9)

    universe = Universe(dimensions=3)
    universe.add_body(sphere)
    universe.add_body(point)

    W = universe.get_electrical_work_over('point', point_0, point_1)

    assert compare_floats(3.393E-8, W)