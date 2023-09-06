from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance


class GravitationalPotentialEnergyEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def _equation(self, main_body):

        foo = 0.0

        # equation to solve is Ep_t + G*Sum_i M_i*Sum_j=i+1 m_j/d_j = 0
        
        for idx, main_body in enumerate(self.universe.bodies[:-1]):
            for body in self.universe.bodies[idx+1:]:
                
                dist = distance(body.position.value, main_body.position.value)
                foo += body.mass.value/dist

            foo *= G*main_body.mass.value
        
        # TODO this is not the Ep of one body but the whole system
        # I could indent it once but then there will be many Ep unknowns
        foo += main_body.gravitational_potential_energy.value
        
        return Equation(foo)
    
    def solve(self, main_body, unknown):

        equation = self._equation(main_body)

        return equation.solve(unknown)
