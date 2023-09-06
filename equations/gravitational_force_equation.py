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
                alpha = angle_with_horizontal(body.position(), main_body.position())
                dist = distance(body.position(), main_body.position())
                foo += body.mass()/dist**2

        foo *= G*main_body.mass()
        foo *= math.cos(alpha) if axis == 0 else math.sin(alpha)  # TODO what about 3D?
        foo += main_body.gravitational_force[axis]
        
        return Equation(foo)
    
    def solve(self, body, unknown, axis=None, first_positive_root=False):

        if unknown == 'p':
            raise RuntimeError(f'Equation cannot be solved for unknown \'p\'')

        if axis:

            if axis not in self.axes.components.keys():
                raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

            root = self._solve_one_axis(body, unknown, axis, first_positive_root)

        else:

            root = self._solve_all_axes(body, unknown, first_positive_root)

        return root

    def _solve_one_axis(self, body, unknown, axis, first_positive_root):

        axis = self.axes.components[axis]
        equation = self._equation(body, axis)
        root = equation.solve(unknown, first_positive_root)

        return root

    def _solve_all_axes(self, body, unknown, first_positive_root):

        roots = list()

        for axis in self.axes.components.keys():

            root = self._solve_one_axis(body, unknown, axis, first_positive_root)
            roots.append(root)

        return tuple(roots)
