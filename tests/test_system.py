import sys
import math
from sympy import Symbol

sys.path.append(r'/home/cmesado/Dropbox/dev')

from physics.utils import compare_floats
from physics.drivers.equation import Equation
from physics.drivers.system import System


def test_system():

    n = Symbol('n')
    y1 = Symbol('y1')
    y2 = Symbol('y2')

    equation_0 = Equation(165*y1 - 0.310*n - 0.517*n)
    equation_1 = Equation(165*y2 - 0.173*n - 0.517*n)
    equation_2 = Equation(y1 + y2 - 1.0)

    system = System()
    system.add_equation(equation_0)
    system.add_equation(equation_1)
    system.add_equation(equation_2)

    unknowns = ['n', 'y1', 'y2']

    n, y1, y2 = system.solve(unknowns)

    assert compare_floats(n, 108.77)
    assert compare_floats(y1, 0.55)
    assert compare_floats(y2, 0.45)
