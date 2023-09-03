from scipy.constants import G

from .body import Body
from ..equations.gravitational_force_law import GravitationalForceLaw
from ..equations.gravitational_potential_energy_law import GravitationalPotentialEnergyLaw
from ..equations.gravitational_field_intensity_law import GravitationalFieldIntensityLaw
from ..equations.gravitational_potential_law import GravitationalPotentialLaw
from ..utils import distance


class Field:

    def __init__(self, dimensions=2):

        if dimensions < 1 or dimensions > 3:
            raise ValueError('Parameter \'dimensions\' must be between 1 and 3')
        
        self.dimensions = dimensions

        self.bodies = list()

        # define equations

        self.gravitational_force_equation = GravitationalForceLaw(self)
        self.gravitational_potential_energy_equation = GravitationalPotentialEnergyLaw(self)
        self.gravitational_field_intensity_equation = GravitationalFieldIntensityLaw(self)
        self.gravitational_potential_equation = GravitationalPotentialLaw(self)

    def add_body(self, body):

        if not isinstance(body, Body):
            raise ValueError(f'Cannot add object of type {type(body)}')
        
        self.bodies.append(body)

    def get_body(self, name):

        body = [body for body in self.bodies if body.name == name]

        if not body:
            raise ValueError(f'Body with name {name} not found')
        
        return body[0]

    def solve_gravitational_force_equation(self, name, unknown):

        body = self.get_body(name)

        return self.gravitational_force_equation.solve(body, unknown)

    def solve_gravitational_potential_energy_equation(self, name, unknown):

        body = self.get_body(name)

        return self.gravitational_potential_energy_equation.solve(body, unknown)

    def solve_gravitational_field_intensity_equation(self, point, unknown):

        return self.gravitational_field_intensity_equation.solve(point, unknown)

    def solve_gravitational_potential_equation(self, point, unknown):

        return self.gravitational_potential_equation.solve(point, unknown)

    def get_gravitational_force_over(self, name):

        body = self.get_body(name)

        return self.gravitational_force_equation.solve(body, 'Fg')[0]

    def get_gravitational_potential_energy_over(self, name):

        body = self.get_body(name)

        return self.gravitational_potential_energy_equation.solve(body, 'Ug')[0]

    def get_gravitational_field_intensity_in(self, point):

        return self.gravitational_field_intensity_equation.solve(point, 'gg')[0]

    def get_gravitational_potential_in(self, point):

        return self.gravitational_potential_equation.solve(point, 'Vg')[0]


