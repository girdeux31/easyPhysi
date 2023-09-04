
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class LinearVelocityEquation:
    
    def __init__(self, body):

        self.body = body
        self.axes = Axes(self.body.dimensions)
    
    def _equation(self, axis):

        # equation to solve is v0-v + g*t = 0
        
        foo = self.body.initial_velocity.value[axis] - self.body.velocity.value[axis] \
                    + self.body.gravity.value[axis]*self.body.time.value

        return Equation(foo)

    def solve(self, unknown, axis):

        if axis not in self.axes.components.keys():
            raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

        axis = self.axes.components[axis]
        equation = self._equation(axis)

        return equation.solve(unknown)  # TODO return for all axis as tuple?