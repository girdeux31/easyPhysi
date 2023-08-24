from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance


class GravitationLaw:
    
    def __init__(self, filed):

        self.field = filed
        self.axes = Axes(self.field.dimensions)

    def _equation(self, _body, axis):

        foo = 0.0
        axis = self.axes.components[axis]

        # equation to solve is Fab + G*M*Sum mi/d**2  = 0
        
        for body in self.field.bodies:
            if body is not _body:
                
                dist = distance(_body.position.value, body.position.value)
                foo += body.mass.value/dist**2

        foo *= G*_body.mass.value
        foo += _body.gravity_force.value
        
        return Equation(foo)
    
    def solve(self, _body, unknown, axis):

        if axis not in self.axes.components.keys():
            raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

        equation = self._equation(_body, axis)

        return equation.solve(unknown)
