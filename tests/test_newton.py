
import sys
import math
from sympy import Symbol, solve
from sympy.abc import a

sys.path.append(r'/home/cmesado/Dropbox/dev')
sys.path.append(r'C:\Users\cmem\onedrive_cmem\OneDrive - ENUSA Industrias Avanzadas, S.A., S.M.E\python')

from physics.drivers.body import Body


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

    body = Body(dimensions=2)

    body.set('mass', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    a = body.solve_newton_equation('a', axis='x')
    assert a

    f = m*a[0].subs('mu', 0.0)
    assert str(round(f, 2)) == '-1036.47'

    f = m*a[0].subs('mu', 0.1)
    assert str(round(f, 2)) == '-1258.74'

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

    body = Body(dimensions=2)

    body.set('mass', m)
    body.apply_force('W', W)
    body.apply_force('Fr', Fr)
    body.apply_force('N', N)

    a = body.solve_newton_equation('a', axis='x')
    assert a

    f = m*a[0]
    assert str(round(f, 2)) == '-1258.74'

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
    body_a = Body()
    body_a.set('mass', ma)
    body_a.apply_force('T2', Tab)
    body_a.apply_force('Fra', Fra)
    body_a.apply_force('Wa', Wa)

    body_b = Body()
    body_b.set('mass', mb)
    body_b.apply_force('T1', Tbc)
    body_b.apply_force('T2', Tba)
    body_b.apply_force('Frb', Frb)

    body_c = Body()
    body_c.set('mass', mc)
    body_c.apply_force('Wc', Wc)
    body_c.apply_force('T1', Tcb)

    # Solve a for each body
    aa = body_a.solve_newton_equation('a', axis='x')
    ab = body_b.solve_newton_equation('a', axis='x')
    ac = body_c.solve_newton_equation('a', axis='x')

    solution = solve([aa[0]-Symbol('a'), ab[0]-Symbol('a'), ac[0]-Symbol('a')], ['T1', 'T2', 'a'])
    
    assert solution
    assert str(round(solution[a], 2)) == '0.79'

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
    body = Body()
    body.set('mass', ma+mb+mc)
    body.apply_force('T2', Tab)
    body.apply_force('Fra', Fra)
    body.apply_force('Wa', Wa)
    body.apply_force('T1', Tbc)
    body.apply_force('T2', Tba)
    body.apply_force('Frb', Frb)
    body.apply_force('Wc', Wc)
    body.apply_force('T1', Tcb)

    # Solve for a
    a = body.solve_newton_equation('a', axis='x')
    
    assert a
    assert str(round(a[0], 2)) == '0.79'

