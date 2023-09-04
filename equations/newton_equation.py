
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class NewtonEquation:
    
    def __init__(self, body):

        self.body = body
        self.axes = Axes(self.body.dimensions)

    def _equation(self, axis):

        foo = 0.0

        # equation to solve is \sum F - m*a = 0
        
        for force in self.body.forces:
            foo += force.value[axis]

        foo -= self.body.mass.value*self.body.acceleration.value[axis]
        
        return Equation(foo)
    
    def solve(self, unknown, axis):

        if axis not in self.axes.components.keys():
            raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

        axis = self.axes.components[axis]
        equation = self._equation(axis)

        return equation.solve(unknown)  # TODO return for all axis as tuple?
