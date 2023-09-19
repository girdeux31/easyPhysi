
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class EnergyEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def __call__(self, name):

        return self.equation(name)

    def _equation(self, body):

        foo = 0.0

        # equation to solve is \sum E = 0
        
        for energy in body.energies:
            foo += energy()
        
        return Equation(foo)
    
    def equation(self, name):

        body = self.universe.get_body(name)
        equation = self._equation(body)

        return equation
