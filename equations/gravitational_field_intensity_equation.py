import math
from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance, angle_with_horizontal


class GravitationalFieldIntensityEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def _equation(self, point, axis):

        foo = 0.0

        # equation to solve is g_t + G*Sum_i m_i/d_i**2  = 0
        
        for body in self.universe.bodies:
                
            # array from body to point since we want to measure the angle between horizontal and point
            alpha = angle_with_horizontal(body.position(), point)
            dist = distance(body.position(), point)
            foo += G*body.mass()/dist**2

        foo *= math.cos(alpha) if axis == 0 else math.sin(alpha)  # TODO what about 3D?
        foo += body.gravitational_field_intensity[axis]
        
        return Equation(foo)
       
    def solve(self, point, unknown, axis=None, first_positive_root=False):

        if not hasattr(point, '__len__') or len(point) != self.universe.dimensions:
            raise ValueError(f'Parameter \'point\' must have length {self.universe.dimensions}')

        if unknown == 'p':
            raise RuntimeError(f'Equation cannot be solved for unknown \'p\'')

        if axis:

            if axis not in self.axes.components.keys():
                raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

            root = self._solve_one_axis(point, unknown, axis, first_positive_root)

        else:

            root = self._solve_all_axes(point, unknown, first_positive_root)

        return root

    def _solve_one_axis(self, point, unknown, axis, first_positive_root):

        axis = self.axes.components[axis]
        equation = self._equation(point, axis)
        root = equation.solve(unknown, first_positive_root)

        return root

    def _solve_all_axes(self, point, unknown, first_positive_root):

        roots = list()

        for axis in self.axes.components.keys():

            root = self._solve_one_axis(point, unknown, axis, first_positive_root)
            roots.append(root)

        return tuple(roots)