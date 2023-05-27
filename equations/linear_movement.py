
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class LinearMovement:
    
    def __init__(self, body):

        self.body = body
        self.axes = Axes(self.body.dimensions)

    def _get_position_equation(self, axis):

        axis = self.axes.components[axis]

        # equation to solve is p0-p + v0*t + 1/2*g*t**2 = 0
        foo = self.body.initial_position.value[axis] - self.body.position.value[axis] \
                    + self.body.initial_velocity.value[axis]*self.body.time.value \
                    + self.body.gravity.value[axis]/2*self.body.time.value**2
        
        return Equation(foo)
    
    def _get_velocity_equation(self, axis):

        axis = self.axes.components[axis]

        # equation to solve is v0-v + g*t = 0
        foo = self.body.initial_velocity.value[axis] - self.body.velocity.value[axis] \
                    + self.body.gravity.value[axis]*self.body.time.value

        return Equation(foo)

    def solve_position_equation(self, unknown, axis):

        if axis not in self.axes.components.keys():
            raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

        equation = self._get_position_equation(axis)

        return equation.solve(unknown)  # TODO return for all axis as tuple?
    
    def solve_velocity_equation(self, unknown, axis):

        if axis not in self.axes.components.keys():
            raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

        equation = self._get_velocity_equation(axis)

        return equation.solve(unknown)  # TODO return for all axis as tuple?