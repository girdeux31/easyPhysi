from scipy.constants import G

from .body import Body
from ..equations.gravitational_force_law import GravitationalForceLaw
from ..equations.gravitational_potential_energy_law import GravitationalPotentialEnergyLaw
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

    def add_body(self, body):

        if not isinstance(body, Body):
            raise ValueError(f'Cannot add object of type {type(body)}')
        
        self.bodies.append(body)

    def get_body(self, name):

        body = [body for body in self.bodies if body.name == name]

        if not body:
            raise ValueError(f'Body with name {name} not found')
        
        return body[0]

    def solve_gravitational_force_equation(self, name, unknown, axis='x'):

        body = self.get_body(name)

        return self.gravitational_force_equation.solve(body, unknown, axis)

    def solve_gravitational_potential_energy_equation(self, name, unknown, axis='x'):

        body = self.get_body(name)

        return self.gravitational_potential_energy_equation.solve(body, unknown, axis)

    def get_gravitational_force_over(self, name):

        foo = 0.0
        main_body = self.get_body(name)
        
        for body in self.bodies:
            if body is not main_body:
                
                dist = distance(main_body.position.value, body.position.value)
                foo += body.mass.value/dist**2

        foo *= -G*main_body.mass.value
        
        return foo

    def get_gravitational_potential_energy_over(self, name):

        foo = 0.0
        main_body = self.get_body(name)
        
        for body in self.bodies:
            if body is not main_body:
                
                dist = distance(main_body.position.value, body.position.value)
                foo += body.mass.value/dist

        foo *= -G*main_body.mass.value
        
        return foo


