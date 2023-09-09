import math

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance, angle_with_horizontal_2d, K


class ElectricalForceEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def __call__(self, name, axis=None):

        return self.equation(name, axis=axis)

    def _equation(self, main_body, axis):

        foo = 0.0

        # equation to solve is Fe_t - K*Q*Sum_i q_i/d_i**2  = 0
        
        for body in self.universe.bodies:
            if body is not main_body:
                
                # array from body to main_body since we want to measure the angle between horizontal axis and main body

                if self.universe.dimensions == 2:
                    alpha = angle_with_horizontal_2d(body.position(), main_body.position())
                else:  # 3D
                    alpha, beta = alpha = angle_with_horizontal_3d(body.position(), main_body.position())

                dist = distance(body.position(), main_body.position())
                factor = math.cos(alpha) if axis == 0 else math.sin(alpha) if axis == 1 else math.sin(beta)
                foo -= K*main_body.charge()*body.charge()/dist**2 * factor

        foo += main_body.electrical_force[axis]
        
        return Equation(foo)

    def equation(self, name, axis=None):

        # if unknown == 'p':  # TODO move where to?
        #     raise RuntimeError(f'Equation cannot be solved for unknown \'p\'')

        body = self.universe.get_body(name)

        if axis:

            if axis not in self.axes.components.keys():
                raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

            equation = self._equation_for_one_axis(body, axis)

        else:

            equation = self._equations_for_all_axes(body)

        return equation

    def _equation_for_one_axis(self, body, axis):

        axis = self.axes.components[axis]
        equation = self._equation(body, axis)

        return equation

    def _equations_for_all_axes(self, body):

        equations = list()

        for axis in self.axes.components.keys():

            equation = self._equation_for_one_axis(body, axis)
            equations.append(equation)

        return tuple(equations)
