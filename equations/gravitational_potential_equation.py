from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance


class GravitationalPotentialEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def _equation(self, point):

        foo = 0.0

        # equation to solve is V_t + G*Sum_i m_i/d_i  = 0
        
        for body in self.universe.bodies:
                
            dist = distance(body.position.value, point)
            foo += G*body.mass.value/dist

        foo += body.gravitational_potential.value
        
        return Equation(foo)
    
    def solve(self, point, unknown, first_positive_root=False):

        if not hasattr(point, '__len__') or len(point) != self.universe.dimensions:
            raise ValueError(f'Parameter \'point\' must have length {self.universe.dimensions}')

        equation = self._equation(point)
        root = equation.solve(unknown, first_positive_root)

        return root
