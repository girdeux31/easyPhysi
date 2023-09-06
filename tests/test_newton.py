
import sys
import math
from sympy import Symbol, solve
from sympy.abc import a

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.drivers.body import Body
from physics.drivers.universe import Universe
from physics.utils import compare_floats


def test_newton_i():
    """
    Relación 8 las fuerzas
    Problema 14
    """
    mu = Symbol('mu')
    alpha = math.radians(25)
    m = 250
    g = 9.81
    W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
    N = (0.0, m*g*math.sin(alpha))
    Fr = (-mu*m*g*math.cos(alpha), 0.0)

    body = Body('A', dimensions=2)

    body.set('mass', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    universe = Universe()
    universe.add_body(body)

    a = universe.solve_newton_equation('A', 'a')  # TODO simply
    f_00 = m*a[0][0].subs('mu', 0.0)
    f_01 = m*a[0][0].subs('mu', 0.1)

    assert a
    assert compare_floats(f_00, -1036.47)
    assert compare_floats(f_01, -1258.74)

def test_newton_ii():
    """
    Relación 8 las fuerzas
    Problema 14
    """
    mu = 0.1
    alpha = math.radians(25)
    m = 250
    g = 9.81
    W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
    N = (0.0, m*g*math.sin(alpha))
    Fr = (-mu*m*g*math.cos(alpha), 0.0)

    body = Body('A', dimensions=2)

    body.set('mass', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    universe = Universe()
    universe.add_body(body)

    a = universe.solve_newton_equation('A', 'a', axis='x')
    f = m*a[0]

    assert compare_floats(a[0], -5.03)    
    assert compare_floats(f, -1258.74)

def test_newton_iii():
    """
    Examen cinemática y dinámica
    Problema 8
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
    body_a = Body('A')
    body_a.set('mass', ma)
    body_a.apply_force('T2', Tab)
    body_a.apply_force('Fra', Fra)
    body_a.apply_force('Wa', Wa)

    body_b = Body('B')
    body_b.set('mass', mb)
    body_b.apply_force('T1', Tbc)
    body_b.apply_force('T2', Tba)
    body_b.apply_force('Frb', Frb)

    body_c = Body('C')
    body_c.set('mass', mc)
    body_c.apply_force('Wc', Wc)
    body_c.apply_force('T1', Tcb)

    universe = Universe()
    universe.add_body(body_a)
    universe.add_body(body_b)
    universe.add_body(body_c)

    # Solve a for each body
    aa = universe.solve_newton_equation('A', 'a', axis='x')
    ab = universe.solve_newton_equation('B', 'a', axis='x')
    ac = universe.solve_newton_equation('C', 'a', axis='x')

    solution = solve([aa[0]-Symbol('a'), ab[0]-Symbol('a'), ac[0]-Symbol('a')], ['T1', 'T2', 'a'])
    
    assert solution
    assert compare_floats(solution[a], 0.79)

def test_newton_iv():
    """
    Examen cinemática y dinámica
    Problema 8
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
    body = Body('A')
    body.set('mass', ma+mb+mc)
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
    a = universe.solve_newton_equation('A', 'a', axis='x', first_positive_root=True)
    
    assert compare_floats(a, 0.79)

