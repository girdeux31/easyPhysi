
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class EnergyLaw:
    
    def __init__(self, body):

        self.body = body
        self.axes = Axes(self.body.dimensions)

    def _get_energy_equation(self):

        foo = 0.0

        # equation to solve is \sum E = 0
        for energy in self.body.energies:
            foo += energy.value
        
        return Equation(foo)
    
    def solve_energy_equation(self, unknown):

        equation = self._get_energy_equation()

        return equation.solve(unknown)
