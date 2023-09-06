import math
from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance, angle_with_horizontal


class GravitationalForceEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def _equation(self, main_body, axis):

        foo = 0.0

        # equation to solve is F_t + G*M*Sum_i m_i/d_i**2  = 0
        
        for body in self.universe.bodies:
            if body is not main_body:
                
                # array from body to main_body since we want to measure the angle between horizontal and main body
                alpha = angle_with_horizontal(body.position.value, main_body.position.value)
                dist = distance(body.position.value, main_body.position.value)
                foo += body.mass.value/dist**2

        foo *= G*main_body.mass.value
        foo *= math.cos(alpha) if axis == 0 else math.sin(alpha)  # TODO what about 3D?
        foo += main_body.gravitational_force.value[axis]
        
        return Equation(foo)
    
    def solve(self, main_body, unknown, axis):

        if unknown == 'p':
            raise RuntimeError(f'Equation cannot be solved for unknown \'p\'')

        if axis not in self.axes.components.keys():
            raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

        axis = self.axes.components[axis]
        equation = self._equation(main_body, axis)

        return equation.solve(unknown)  # TODO return for all axis as tuple?
