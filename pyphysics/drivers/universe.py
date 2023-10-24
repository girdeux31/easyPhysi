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

        self.electrical_field_intensity_equation = ElectricalFieldIntensityEquation(self)
        self.electrical_force_equation = ElectricalForceEquation(self)
        self.electrical_potential_energy_equation = ElectricalPotentialEnergyEquation(self)
        self.electrical_potential_equation = ElectricalPotentialEquation(self)
        self.energy_equation = EnergyEquation(self)
        self.gravitational_field_intensity_equation = GravitationalFieldIntensityEquation(self)
        self.gravitational_force_equation = GravitationalForceEquation(self)
        self.gravitational_potential_energy_equation = GravitationalPotentialEnergyEquation(self)
        self.gravitational_potential_equation = GravitationalPotentialEquation(self)
        self.linear_position_equation = LinearPositionEquation(self)
        self.linear_velocity_equation = LinearVelocityEquation(self)
        self.newton_equation = NewtonEquation(self)

    def add_body(self, body):

        if not isinstance(body, Body):
            raise TypeError(f'Cannot add object of type {type(body).__name__}')

        if body.dimensions != self.dimensions:
            raise ValueError(f'Body dimensions {body.dimensions} and universe dimensions {self.dimensions} mismatch')
        
        self.bodies.append(body)

    def get_body(self, name):

        body = [body for body in self.bodies if body.name == name]

        if not body:
            raise ValueError(f'Body with name {name} not found')
        
        return body[0]

    def help(self):  #TODO what about force and energy?

        print('The following equations are recognized:')
        print('')
        print(' {:40s} {:10s} {:16s}'.format('Equation', 'Type', 'Parameters'))
        print(' ' + '='*40 + ' ' + '='*10 + ' '+ '='*16)

        for key, value in self.__dict__.items():

            if hasattr(value, '_equation'):
                type_ = 'Scalar' if hasattr(value, 'equation') else 'Vectorial'
                print(f' {key:40s} {type_:10s} {value.parameters}')

        print('')