
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class NewtonLaw:
    
    def __init__(self, body):

        self.body = body
        self.axes = Axes(self.body.dimensions)

    def _get_newton_equation(self, axis):

        foo = 0.0
        axis = self.axes.components[axis]

        # equation to solve is \sum F - m*a = 0
        for force in self.body.forces:
            foo += force.value[axis]

        foo -= self.body.mass.value*self.body.acceleration.value[axis]
        
        return Equation(foo)  # TODO return for all axis as tuple?
    
    def solve_newton_equation(self, unknown, axis):

        if axis not in self.axes.components.keys():
            raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

        equation = self._get_newton_equation(axis)

        return equation.solve(unknown)
