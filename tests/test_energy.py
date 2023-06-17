
import sys
import math
from sympy import Symbol

sys.path.append(r'/home/cmesado/Dropbox/dev')
sys.path.append(r'C:\Users\cmem\onedrive_cmem\OneDrive - ENUSA Industrias Avanzadas, S.A., S.M.E\python')

from physics.drivers.body import Body


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

    body = Body(dimensions=2)

    body.add_energy('Ep0', Ep0)
    body.add_energy('Ec0', Ek0)
    body.add_energy('Epf', Epf)
    body.add_energy('Ecf', Ekf)

    vf = body.solve_energy_equation('vf')

    assert vf
    assert str(round(vf[1], 2)) == '4.54'


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

    body = Body(dimensions=2)

    body.add_energy('Ep0', Ep0)
    body.add_energy('Ec0', Ek0)
    body.add_energy('Epf', Epf)
    body.add_energy('Ecf', Ekf)
    body.add_energy('Epe', Epe)

    dx = body.solve_energy_equation('dx')

    assert dx
    assert str(round(dx[1], 3)) == '0.227'


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

    body = Body(dimensions=2)

    body.add_energy('Ep0', Ep0)
    body.add_energy('Ec0', Ek0)
    body.add_energy('Epf', Epf)
    body.add_energy('Ecf', Ekf)
    body.add_energy('Wfr', Wfr)

    vf = body.solve_energy_equation('vf')

    assert vf
    assert str(round(vf[1], 2)) == '3.72'
