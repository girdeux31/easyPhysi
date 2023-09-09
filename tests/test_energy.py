
import sys
import math
from sympy import Symbol

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.body import Body
from physics.drivers.universe import Universe
from physics.utils import compare_floats


def test_energy_15a():
    """
    15 problemas trabajo y energia mecanica
    Problema 15.a
    """
    m = 1.0
    v0 = 1.0
    alpha = math.radians(30)
    length = 2.0
    g = 9.81
    h0 = length*math.sin(alpha)
    hf = 0.0
    vf = Symbol('vf')

    Ep0 = m*g*h0
    Ek0 = 1/2*m*v0**2
    Epf = -m*g*hf
    Ekf = -1/2*m*vf**2

    body = Body('body', dimensions=2)

    body.add_energy('Ep0', Ep0)
    body.add_energy('Ek0', Ek0)
    body.add_energy('Epf', Epf)
    body.add_energy('Ekf', Ekf)

    universe = Universe()
    universe.add_body(body)

    vf = universe.energy_equation('body').solve('vf', first_positive_root=True)

    assert compare_floats(vf, 4.54)

    vf = universe.energy_equation('body').solve('vf')

    assert compare_floats(vf[0], -4.54)
    assert compare_floats(vf[1], 4.54)

def test_energy_15b():
    """
    15 problemas trabajo y energia mecanica
    Problema 15.b
    """
    m = 0.5
    k = 200.0
    v0 = 1.0
    alpha = math.radians(30)
    length = 2.0
    g = 9.81
    h0 = length*math.sin(alpha)
    hf = 0.0
    vf = 0.0
    dx = Symbol('dx')

    Ep0 = m*g*h0
    Ek0 = 1/2*m*v0**2
    Epf = -m*g*hf
    Ekf = -1/2*m*vf**2
    Epe = -1/2*k*dx**2

    body = Body('body', dimensions=2)

    body.add_energy('Ep0', Ep0)
    body.add_energy('Ek0', Ek0)
    body.add_energy('Epf', Epf)
    body.add_energy('Ekf', Ekf)
    body.add_energy('Epe', Epe)

    universe = Universe()
    universe.add_body(body)

    dx = universe.energy_equation('body').solve('dx', first_positive_root=True)

    assert compare_floats(dx, 0.227, decimals=3)

    dx = universe.energy_equation('body').solve('dx')

    assert compare_floats(dx[0], -0.227, decimals=3)
    assert compare_floats(dx[1], 0.227, decimals=3)

def test_energy_15c():
    """
    15 problemas trabajo y energia mecanica
    Problema 15.c
    """
    m = 0.5
    v0 = 1.0
    alpha = math.radians(30)
    length = 2.0
    g = 9.81
    h0 = length*math.sin(alpha)
    hf = 0.0
    vf = 0.0
    mu = 0.2
    vf = Symbol('vf')

    Ep0 = m*g*h0
    Ek0 = 1/2*m*v0**2
    Epf = -m*g*hf
    Ekf = -1/2*m*vf**2
    Wfr = -mu*m*g*math.cos(alpha)*length

    body = Body('body', dimensions=2)

    body.add_energy('Ep0', Ep0)
    body.add_energy('Ek0', Ek0)
    body.add_energy('Epf', Epf)
    body.add_energy('Ekf', Ekf)
    body.add_energy('Wfr', Wfr)

    universe = Universe()
    universe.add_body(body)

    vf = universe.energy_equation('body').solve('vf', first_positive_root=True)

    assert compare_floats(vf, 3.72)

    vf = universe.energy_equation('body').solve('vf')

    assert compare_floats(vf[0], -3.72)
    assert compare_floats(vf[1], 3.72)

def test_energy_20a():
    """
    15 problemas trabajo y energia mecanica
    Problema 20a
    """
    m = 3.0
    ha = 4.0
    hb = 0.0
    va = 0.0
    vb = Symbol('vb')
    g = 9.81

    Epa = m*g*ha
    Eka = 1/2*m*va**2
    Epb = -m*g*hb
    Ekb = -1/2*m*vb**2

    body = Body('body', dimensions=2)

    body.add_energy('Epa', Epa)
    body.add_energy('Eka', Eka)
    body.add_energy('Epb', Epb)
    body.add_energy('Ekb', Ekb)

    universe = Universe()
    universe.add_body(body)

    vb = universe.energy_equation('body').solve('vb', first_positive_root=True)

    assert compare_floats(vb, 8.86)

    vb = universe.energy_equation('body').solve('vb')

    assert compare_floats(vb[0], -8.86)
    assert compare_floats(vb[1], 8.86)

def test_energy_20c():
    """
    15 problemas trabajo y energia mecanica
    Problema 20c
    """
    m = 3.0
    hc = 0.0
    hb = 0.0
    vc = 0.0
    vb = 8.86
    x = 10.0
    g = 9.81
    mu = Symbol('mu')

    Epb = m*g*hb
    Ekb = 1/2*m*vb**2
    Epc = -m*g*hc
    Ekc = -1/2*m*vc**2
    Wfr = -mu*m*g*x

    body = Body('body', dimensions=2)

    body.add_energy('Epb', Epb)
    body.add_energy('Ekb', Ekb)
    body.add_energy('Epa', Epc)
    body.add_energy('Eka', Ekc)
    body.add_energy('Wfr', Wfr)

    universe = Universe()
    universe.add_body(body)

    mu = universe.energy_equation('body').solve('mu', first_positive_root=True)

    assert compare_floats(mu, 0.40)
