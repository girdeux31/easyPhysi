
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class EnergyEquation:
    
    def __init__(self, body):

        self.body = body
        self.axes = Axes(self.body.dimensions)

    def _equation(self):

        foo = 0.0

        # equation to solve is \sum E = 0
        
        for energy in self.body.energies:
            foo += energy.value
        
        return Equation(foo)
    
    def solve(self, unknown):

        equation = self._equation()

        return equation.solve(unknown)
