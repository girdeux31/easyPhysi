import math
from scipy.constants import G

from .body import Body
from ..equations.linear_position_equation import LinearPositionEquation
from ..equations.linear_velocity_equation import LinearVelocityEquation
from ..equations.newton_equation import NewtonEquation
from ..equations.energy_equation import EnergyEquation
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

        self.linear_position_equation = LinearPositionEquation(self)
        self.linear_velocity_equation = LinearVelocityEquation(self)
        self.newton_equation = NewtonEquation(self)
        self.energy_equation = EnergyEquation(self)
        self.gravitational_force_equation = GravitationalForceEquation(self)
        self.gravitational_potential_energy_equation = GravitationalPotentialEnergyEquation(self)
        self.gravitational_field_intensity_equation = GravitationalFieldIntensityEquation(self)
        self.gravitational_potential_equation = GravitationalPotentialEquation(self)
        self.electrical_force_equation = ElectricalForceEquation(self)
        self.electrical_potential_energy_equation = ElectricalPotentialEnergyEquation(self)
        self.electrical_field_intensity_equation = ElectricalFieldIntensityEquation(self)
        self.electrical_potential_equation = ElectricalPotentialEquation(self)

    def add_body(self, body):

        if not isinstance(body, Body):
            raise ValueError(f'Cannot add object of type {type(body)}')

        if body.dimensions != self.dimensions:
            raise ValueError(f'Body dimensions {body.dimensions} and universe dimensions {self.dimensions} mismatch')
        
        self.bodies.append(body)

    def get_body(self, name):

        body = [body for body in self.bodies if body.name == name]

        if not body:
            raise ValueError(f'Body with name {name} not found')
        
        return body[0]

    #######
    # SOLVE
    #######

    # Uniformly Accelerated Rectilinear Motion (UARM)

    def solve_linear_position_equation(self, name, unknown, axis=None, first_positive_root=False):

        body = self.get_body(name)

        return self.linear_position_equation.solve(body, unknown, axis, first_positive_root)  # vectorial equation
    
    def solve_linear_velocity_equation(self, name, unknown, axis=None, first_positive_root=False):

        body = self.get_body(name)

        return self.linear_velocity_equation.solve(body, unknown, axis, first_positive_root)  # vectorial equation

    # Dynamics (Newton's equation)

    def solve_newton_equation(self, name, unknown, axis=None, first_positive_root=False):

        body = self.get_body(name)

        return self.newton_equation.solve(body, unknown, axis, first_positive_root)  # vectorial equation

    # Energy conservation equation

    def solve_energy_equation(self, name, unknown, first_positive_root=False):

        body = self.get_body(name)

        return self.energy_equation.solve(body, unknown, first_positive_root)  # scalar equation

    # Gravitational field

    def solve_gravitational_force_equation(self, name, unknown, axis=None, first_positive_root=False):

        body = self.get_body(name)

        return self.gravitational_force_equation.solve(body, unknown, axis, first_positive_root)  # vectorial equation

    def solve_gravitational_potential_energy_equation(self, name, unknown, first_positive_root=False):

        body = self.get_body(name)

        return self.gravitational_potential_energy_equation.solve(body, unknown, first_positive_root)  # scalar equation

    def solve_gravitational_field_intensity_equation(self, point, unknown, axis=None, first_positive_root=False):

        return self.gravitational_field_intensity_equation.solve(point, unknown, axis, first_positive_root)  # vectorial equation

    def solve_gravitational_potential_equation(self, point, unknown, first_positive_root=False):

        return self.gravitational_potential_equation.solve(point, unknown, first_positive_root)  # scalar equation

    # Electrical Field

    def solve_electrical_force_equation(self, name, unknown, axis=None, first_positive_root=False):

        body = self.get_body(name)

        return self.electrical_force_equation.solve(body, unknown, axis, first_positive_root)  # vectorial equation

    def solve_electrical_potential_energy_equation(self, name, unknown, first_positive_root=False):

        body = self.get_body(name)

        return self.electrical_potential_energy_equation.solve(body, unknown, first_positive_root)  # scalar equation

    def solve_electrical_field_intensity_equation(self, point, unknown, axis=None, first_positive_root=False):

        return self.electrical_field_intensity_equation.solve(point, unknown, axis, first_positive_root)  # vectorial equation

    def solve_electrical_potential_equation(self, point, unknown, first_positive_root=False):

        return self.electrical_potential_equation.solve(point, unknown, first_positive_root)  # scalar equation

    #######
    # GET
    #######

    # TODO get for position, velocity, acceleration and force

    # Gravitational Field

    def get_gravitational_force_over(self, name, axis=None, first_positive_root=False):

        body = self.get_body(name)

        return self.gravitational_force_equation.solve(body, 'Fg', axis, first_positive_root)

    def get_gravitational_potential_energy_over(self, name, first_positive_root=False):

        body = self.get_body(name)

        return self.gravitational_potential_energy_equation.solve(body, 'Ug', first_positive_root)

    def get_gravitational_field_intensity_in(self, point, axis=None, first_positive_root=False):

        return self.gravitational_field_intensity_equation.solve(point, 'gg', axis, first_positive_root)

    def get_gravitational_potential_in(self, point, first_positive_root=False):

        return self.gravitational_potential_equation.solve(point, 'Vg', first_positive_root)

    def get_gravitational_work_over(self, name, point_0, point_1, first_positive_root=False):

        # W = -AEp = Ep_0 - Ep_1

        if not hasattr(point_0, '__len__') or len(point_0) != self.dimensions:
            raise ValueError(f'Parameter \'point_0\' must have length {self.dimensions}')

        if not hasattr(point_1, '__len__') or len(point_1) != self.dimensions:
            raise ValueError(f'Parameter \'point_1\' must have length {self.dimensions}')

        body = self.get_body(name)
        body.set('position', point_0)

        Ep_0 = self.gravitational_potential_energy_equation.solve(body, 'Ug', first_positive_root)

        body.set('position', point_1)
        
        Ep_1 = self.gravitational_potential_energy_equation.solve(body, 'Ug', first_positive_root)

        return Ep_0[0] - Ep_1[0]

    # Electrical Field

    def get_electrical_force_over(self, name, axis=None, first_positive_root=False):

        body = self.get_body(name)
        
        return self.electrical_force_equation.solve(body, 'Fe', axis, first_positive_root)

    def get_electrical_potential_energy_over(self, name, first_positive_root=False):

        body = self.get_body(name)

        return self.electrical_potential_energy_equation.solve(body, 'Ue', first_positive_root)

    def get_electrical_field_intensity_in(self, point, axis=None, first_positive_root=False):

        return self.electrical_field_intensity_equation.solve(point, 'Ee', axis, first_positive_root)

    def get_electrical_potential_in(self, point, first_positive_root=False):

        return self.electrical_potential_equation.solve(point, 'Ve', first_positive_root)

    def get_electrical_work_over(self, name, point_0, point_1, first_positive_root=False):

        # W = -AEp = Ep_0 - Ep_1

        if not hasattr(point_0, '__len__') or len(point_0) != self.dimensions:
            raise ValueError(f'Parameter \'point_0\' must have length {self.dimensions}')

        if not hasattr(point_1, '__len__') or len(point_1) != self.dimensions:
            raise ValueError(f'Parameter \'point_1\' must have length {self.dimensions}')

        body = self.get_body(name)
        body.set('position', point_0)

        Ep_0 = self.electrical_potential_energy_equation.solve(body, 'Ue', first_positive_root)

        body.set('position', point_1)
        
        Ep_1 = self.electrical_potential_energy_equation.solve(body, 'Ue', first_positive_root)

        return Ep_0[0] - Ep_1[0]