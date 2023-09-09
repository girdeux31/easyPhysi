import math
from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance, angle_with_horizontal_2d


class GravitationalFieldIntensityEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def __call__(self, point, axis=None):

        return self.equation(point, axis=axis)

    def _equation(self, point, axis):

        foo = 0.0

        # equation to solve is gg_t + G*Sum_i m_i/d_i**2  = 0
        
        for body in self.universe.bodies:
                
            # array from body to point since we want to measure the angle between horizontal axis and point

            if self.universe.dimensions == 2:
                alpha = angle_with_horizontal_2d(body.position(), point)
            else:  # 3D
                alpha, beta = angle_with_horizontal_3d(body.position(), point)

            dist = distance(body.position(), point)
            factor = math.cos(alpha) if axis == 0 else math.sin(alpha) if axis == 1 else math.sin(beta)
            foo += G*body.mass()/dist**2 * factor
            
        foo += body.gravitational_field_intensity[axis]  # TODO whole system, not only body
        
        return Equation(foo)

    def equation(self, point, axis=None):

        if not hasattr(point, '__len__') or len(point) != self.universe.dimensions:
            raise ValueError(f'Parameter \'point\' must have length {self.universe.dimensions}')

        # if unknown == 'p':  # TODO move where to?
        #     raise RuntimeError(f'Equation cannot be solved for unknown \'p\'')

        if axis:

            if axis not in self.axes.components.keys():
                raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

            equation = self._equation_for_one_axis(point, axis)

        else:

            equation = self._equations_for_all_axes(point)

        return equation

    def _equation_for_one_axis(self, point, axis):

        axis = self.axes.components[axis]
        equation = self._equation(point, axis)

        return equation

    def _equations_for_all_axes(self, point):

        equations = list()

        for axis in self.axes.components.keys():

            equation = self._equation_for_one_axis(point, axis)
            equations.append(equation)

        return tuple(equations)
