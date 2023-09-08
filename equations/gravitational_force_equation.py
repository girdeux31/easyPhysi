import math
from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance, angle_with_horizontal_2d


class GravitationalForceEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def _equation(self, main_body, axis):

        foo = 0.0

        # equation to solve is Fg_t + G*M*Sum_i m_i/d_i**2  = 0
        
        for body in self.universe.bodies:
            if body is not main_body:
                
                # array from body to main_body since we want to measure the angle between horizontal axis and main body

                if self.universe.dimensions == 2:
                    alpha = angle_with_horizontal_2d(body.position(), main_body.position())
                else:  # 3D
                    alpha, beta = alpha = angle_with_horizontal_3d(body.position(), main_body.position())

                dist = distance(body.position(), main_body.position())
                factor = math.cos(alpha) if axis == 0 else math.sin(alpha) if axis == 1 else math.sin(beta)
                foo += G*main_body.mass()*body.mass()/dist**2 * factor
                
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
