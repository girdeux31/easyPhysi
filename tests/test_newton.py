
import sys
import math
from sympy import Symbol

sys.path.append(r'/home/cmesado/Dropbox/dev/pyphysics')

from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.drivers.system import System
from pyphysics.utils import compare_floats


def test_newton_14():
    """
    URL: https://fq.iespm.es/documentos/rafael_artacho/4_ESO/08.%20Problemas%20Las%20fuerzas.pdf
    Problem: 14
    Statement: The following ramp has an inclination of 25º. Determine the force that must be exerted on the 250 kg wagon to make it go up with constant velocity:
    a) If there is no friction.
    b) If 𝜇 = 0.1.
    """
    mu = Symbol('mu')
    alpha = math.radians(25)
    m = 250
    g = 9.81
    W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
    N = (0.0, m*g*math.sin(alpha))
    Fr = (-mu*m*g*math.cos(alpha), 0.0)

    body = Body('body', dimensions=2)

    body.set('m', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    universe = Universe()
    universe.add_body(body)

    a_x, a_y = universe.newton_equation('body').solve(['a_x', 'a_y'])
    f_00 = m*a_x.subs('mu', 0.0)
    f_01 = m*a_x.subs('mu', 0.1)

    assert compare_floats(f_00, -1036.47)
    assert compare_floats(f_01, -1258.74)

def test_newton_14b_bis():
    """
    URL: https://fq.iespm.es/documentos/rafael_artacho/4_ESO/08.%20Problemas%20Las%20fuerzas.pdf
    Problem: 14b
    Statement: The following ramp has an inclination of 25º. Determine the force that must be exerted on the 250 kg wagon to make it go up with constant velocity:
    b) If 𝜇 = 0.1.
    """
    mu = 0.1
    alpha = math.radians(25)
    m = 250
    g = 9.81
    W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
    N = (0.0, m*g*math.sin(alpha))
    Fr = (-mu*m*g*math.cos(alpha), 0.0)

    body = Body('body', dimensions=2)

    body.set('m', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    universe = Universe()
    universe.add_body(body)

    a_x, a_y = universe.newton_equation('body').solve(['a_x', 'a_y'])
    f_x = m*a_x

    assert compare_floats(a_x, -5.03)
    assert compare_floats(a_y, -4.74)
    assert compare_floats(f_x, -1258.74)

def test_newton_8():
    """
    File: Examen cinemática y dinámica
    Problem: 8
    Statement: In the system shown in the figure, the three masses are mA = 1 kg, mB = 2 kg, and mC = 1.5 kg. If the coefficient of friction is 𝜇 = 0.223, calculate the acceleration of the system when it is released.
    """
    # initialize parameters and constants
    g = 9.81
    mu = 0.223
    alpha = math.radians(30)
    ma, mb, mc = 1, 2, 1.5

    # define known forces
    Fra = (-mu*ma*g*math.cos(alpha), 0.0)
    Frb = (-mu*mb*g, 0.0)
    Wa = (-ma*g*math.sin(alpha), -ma*g*math.cos(alpha))
    Wc = (mc*g, 0.0)

    # define unknown forces
    Tab = (Symbol('T2'), 0.0)
    Tba = (-Symbol('T2'), 0.0)
    Tbc = (Symbol('T1'), 0.0)
    Tcb = (-Symbol('T1'), 0.0)
    
    # define bodies and apply forces
    body_a = Body('A')
    body_a.set('m', ma)
    body_a.apply_force('T2', Tab)
    body_a.apply_force('Fra', Fra)
    body_a.apply_force('Wa', Wa)

    body_b = Body('B')
    body_b.set('m', mb)
    body_b.apply_force('T1', Tbc)
    body_b.apply_force('T2', Tba)
    body_b.apply_force('Frb', Frb)

    body_c = Body('C')
    body_c.set('m', mc)
    body_c.apply_force('Wc', Wc)
    body_c.apply_force('T1', Tcb)

    universe = Universe()
    universe.add_body(body_a)
    universe.add_body(body_b)
    universe.add_body(body_c)

    # Get newton equation for each body

    eq_a = universe.newton_equation('A')['x']
    eq_b = universe.newton_equation('B')['x']
    eq_c = universe.newton_equation('C')['x']

    # Then solve system:

    unkowns = ['T1', 'T2', 'a_x']
    system = System()
    system.add_equation(eq_a)
    system.add_equation(eq_b)
    system.add_equation(eq_c)
    T1, T2, a_x = system.solve(unkowns)
    
    assert compare_floats(T1, 13.54)
    assert compare_floats(T2, 7.59)
    assert compare_floats(a_x, 0.79)

def test_newton_8_bis():
    """
    File: Examen cinemática y dinámica
    Problem: 8
    Statement: In the system shown in the figure, the three masses are mA = 1 kg, mB = 2 kg, and mC = 1.5 kg. If the coefficient of friction is 𝜇 = 0.223, calculate the acceleration of the system when it is released.
    """
    # initialize parameters and constants
    g = 9.81
    mu = 0.223
    alpha = math.radians(30)
    ma = 1
    mb = 2
    mc = 1.5

    # define known forces
    Fra = (-mu*ma*g*math.cos(alpha), 0.0)
    Frb = (-mu*mb*g, 0.0)
    Wa = (-ma*g*math.sin(alpha), -ma*g*math.cos(alpha))
    Wc = (mc*g, 0.0)

    # define unknown forces
    Tab = (Symbol('T2'), 0.0)
    Tba = (-Symbol('T2'), 0.0)
    Tbc = (Symbol('T1'), 0.0)
    Tcb = (-Symbol('T1'), 0.0)
    
    # define bodies and apply forces
    body = Body('body')
    body.set('m', ma+mb+mc)
    body.apply_force('T2', Tab)
    body.apply_force('Fra', Fra)
    body.apply_force('Wa', Wa)
    body.apply_force('T1', Tbc)
    body.apply_force('T2', Tba)
    body.apply_force('Frb', Frb)
    body.apply_force('Wc', Wc)
    body.apply_force('T1', Tcb)

    universe = Universe()
    universe.add_body(body)

    # Solve for a
    a_x, a_y = universe.newton_equation('body').solve(['a_x', 'a_y'])
    
    assert compare_floats(a_x, 0.79)
    assert compare_floats(a_y, -1.89)