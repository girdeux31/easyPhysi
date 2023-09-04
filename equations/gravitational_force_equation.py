from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance


class GravitationalForceEquation:
    
    def __init__(self, field):

        self.field = field
        self.axes = Axes(self.field.dimensions)

    def _equation(self, main_body):

        foo = 0.0

        # equation to solve is F_t + G*M*Sum_i m_i/d_i**2  = 0
        
        for body in self.field.bodies:
            if body is not main_body:
                
                dist = distance(main_body.position.value, body.position.value)
                foo += body.mass.value/dist**2

        foo *= G*main_body.mass.value
        foo += main_body.gravitational_force.value
        
        return Equation(foo)
    
    def solve(self, main_body, unknown):

        equation = self._equation(main_body)

        return equation.solve(unknown)  # TODO return for all axis as tuple?
