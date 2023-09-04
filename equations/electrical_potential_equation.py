from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance, K


class ElectricalPotentialEquation:
    
    def __init__(self, field):

        self.field = field
        self.axes = Axes(self.field.dimensions)

    def _equation(self, point):

        foo = 0.0

        # equation to solve is V_t + K*Sum_i q_i/d_i  = 0
        
        for body in self.field.bodies:
                
            dist = distance(body.position.value, point)
            foo += K*body.charge.value/dist

        foo += body.electrical_potential.value
        
        return Equation(foo)
    
    def solve(self, point, unknown):

        equation = self._equation(point)

        return equation.solve(unknown)
