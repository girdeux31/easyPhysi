from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance


class GravitationalForceLaw:
    
    def __init__(self, filed):

        self.field = filed
        self.axes = Axes(self.field.dimensions)

    def _equation(self, main_body, axis):

        foo = 0.0
        axis = self.axes.components[axis]

        # equation to solve is Fab + G*M*Sum mi/d**2  = 0
        
        for body in self.field.bodies:
            if body is not main_body:
                
                dist = distance(main_body.position.value, body.position.value)
                foo += body.mass.value/dist**2

        foo *= G*main_body.mass.value
        foo += main_body.gravitational_force.value
        
        return Equation(foo)
    
    def solve(self, main_body, unknown, axis):

        if axis not in self.axes.components.keys():
            raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

        equation = self._equation(main_body, axis)

        return equation.solve(unknown)
