import math
from scipy.constants import G

from .body import Body
from ..equations.gravitational_force_equation import GravitationalForceEquation
from ..equations.gravitational_potential_energy_equation import GravitationalPotentialEnergyEquation
from ..equations.gravitational_field_intensity_equation import GravitationalFieldIntensityEquation
from ..equations.gravitational_potential_equation import GravitationalPotentialEquation
from ..equations.electrical_force_equation import ElectricalForceEquation
from ..equations.electrical_potential_energy_equation import ElectricalPotentialEnergyEquation
from ..equations.electrical_field_intensity_equation import ElectricalFieldIntensityEquation
from ..equations.electrical_potential_equation import ElectricalPotentialEquation
from ..utils import distance


class Universe:

    def __init__(self, dimensions=2):

        if dimensions < 1 or dimensions > 3:
            raise ValueError('Parameter \'dimensions\' must be between 1 and 3')
        
        self.dimensions = dimensions

        self.bodies = list()

        # define equations

        self.gravitational_force_equation = GravitationalForceEquation(self)
        self.gravitational_potential_energy_equation = GravitationalPotentialEnergyEquation(self)
        self.gravitational_field_intensity_equation = GravitationalFieldIntensityEquation(self)
        self.gravitational_potential_equation = GravitationalPotentialEquation(self)
        self.electrial_force_equation = ElectricalForceEquation(self)
        self.electrial_potential_energy_equation = ElectricalPotentialEnergyEquation(self)
        self.electrial_field_intensity_equation = ElectricalFieldIntensityEquation(self)
        self.electrial_potential_equation = ElectricalPotentialEquation(self)

    def add_body(self, body):

        if not isinstance(body, Body):
            raise ValueError(f'Cannot add object of type {type(body)}')
        
        self.bodies.append(body)

    def get_body(self, name):

        body = [body for body in self.bodies if body.name == name]

        if not body:
            raise ValueError(f'Body with name {name} not found')
        
        return body[0]

    #######
    # SOLVE
    #######

    def solve_gravitational_force_equation(self, name, unknown, axis='x'):  # TODO None as axis default

        body = self.get_body(name)

        return self.gravitational_force_equation.solve(body, unknown, axis)

    def solve_gravitational_potential_energy_equation(self, name, unknown):

        body = self.get_body(name)  # TODO do i need this?

        return self.gravitational_potential_energy_equation.solve(body, unknown)

    def solve_gravitational_field_intensity_equation(self, point, unknown, axis='x'):

        return self.gravitational_field_intensity_equation.solve(point, unknown, axis)

    def solve_gravitational_potential_equation(self, point, unknown):

        return self.gravitational_potential_equation.solve(point, unknown)

    def solve_electrical_force_equation(self, name, unknown, axis='x'):

        body = self.get_body(name)

        return self.electrical_force_equation.solve(body, unknown, axis)

    def solve_electrical_potential_energy_equation(self, name, unknown):

        body = self.get_body(name)  # TODO do i need this?

        return self.electrical_potential_energy_equation.solve(body, unknown)

    def solve_electrical_field_intensity_equation(self, point, unknown, axis='x'):

        return self.electrical_field_intensity_equation.solve(point, unknown, axis)

    def solve_electrical_potential_equation(self, point, unknown):

        return self.electrical_potential_equation.solve(point, unknown)

    #######
    # GET
    #######

    def get_gravitational_force_over(self, name, axis='x'):

        body = self.get_body(name)
        foo = self.gravitational_force_equation.solve(body, 'Fg', axis)

        return foo[0]

    def get_gravitational_potential_energy_over(self, name):

        body = self.get_body(name)
        foo = self.gravitational_potential_energy_equation.solve(body, 'Ug')

        return foo[0]

    def get_gravitational_field_intensity_in(self, point, axis='x'):

        foo = self.gravitational_field_intensity_equation.solve(point, 'gg', axis)

        return foo[0]

    def get_gravitational_potential_in(self, point):

        foo = self.gravitational_potential_equation.solve(point, 'Vg')

        return foo[0]

    def get_electrical_force_over(self, name, axis='x'):

        body = self.get_body(name)
        foo = self.electrical_force_equation.solve(body, 'Fe', axis)
        
        return foo[0]

    def get_electrical_potential_energy_over(self, name):

        body = self.get_body(name)
        foo = self.electrical_potential_energy_equation.solve(body, 'Ue')

        return foo[0]

    def get_electrical_field_intensity_in(self, point, axis='x'):

        foo = self.electrical_field_intensity_equation.solve(point, 'Ee', axis)

        return foo[0]

    def get_electrical_potential_in(self, point):

        foo = self.electrical_potential_equation.solve(point, 'Ve')

        return foo[0]


