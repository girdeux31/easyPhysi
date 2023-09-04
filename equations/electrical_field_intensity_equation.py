from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance, K


class ElectricalFieldIntensityEquation:
    
    def __init__(self, field):

        self.field = field
        self.axes = Axes(self.field.dimensions)

    def _equation(self, point):

        foo = 0.0

        # equation to solve is E_t + K*Sum_i q_i/d_i**2  = 0
        
        for body in self.field.bodies:
                
            dist = distance(body.position.value, point)
            foo += K*body.charge.value/dist**2

        foo += body.electrical_field_intensity.value
        
        return Equation(foo)
    
    def solve(self, point, unknown):

        equation = self._equation(point)

        return equation.solve(unknown)  # TODO return for all axis as tuple?
