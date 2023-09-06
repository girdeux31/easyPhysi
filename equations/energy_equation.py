
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class EnergyEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def _equation(self, body):

        foo = 0.0

        # equation to solve is \sum E = 0
        
        for energy in body.energies:
            foo += energy.value
        
        return Equation(foo)
    
    def solve(self, body, unknown, first_positive_root=False):

        equation = self._equation(body)
        root = equation.solve(unknown, first_positive_root)

        return root
