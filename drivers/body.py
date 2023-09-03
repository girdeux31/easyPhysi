
from .scalar import Scalar
from .tuple import Tuple
from ..equations.linear_position_law import LinearPositionLaw
from ..equations.linear_velocity_law import LinearVelocityLaw
from ..equations.newton_law import NewtonLaw
from ..equations.energy_law import EnergyLaw


class Body:

    def __init__(self, dimensions=2, name=None):

        if dimensions < 1 or dimensions > 3:
            raise ValueError('Parameter \'dimensions\' must be between 1 and 3')
        
        self.dimensions = dimensions
        self.name = name
        
        self.forces = list()
        self.energies = list()

        # initialize tuples
        
        self.initial_position = Tuple('p0', self.dimensions)
        self.initial_velocity = Tuple('v0', self.dimensions)
        self.position = Tuple('p', self.dimensions)
        self.velocity = Tuple('v', self.dimensions)
        self.gravity = Tuple('g', self.dimensions)
        self.acceleration = Tuple('a', self.dimensions)

        # initialize scalars

        self.mass = Scalar('m')
        self.time = Scalar('t')
        self.charge = Scalar('q')
        self.gravitational_potential_energy = Scalar('Ug')
        self.gravitational_potential = Scalar('Vg')
        self.electrical_potential_energy = Scalar('Ue')
        self.electrical_potential = Scalar('Ve')

        # these are tuples, but handled as scalars so far  # TODO tuples?
        
        self.gravitational_force = Scalar('Fg')
        self.gravitational_field_intensity = Scalar('gg')  # this is the same as gravity 'g'
        self.electrical_force = Scalar('Fe')
        self.electrical_field_intensity = Scalar('Ee')

        # define equations

        self.linear_position_equation = LinearPositionLaw(self)
        self.linear_velocity_equation = LinearVelocityLaw(self)
        self.newton_equation = NewtonLaw(self)
        self.energy_equation = EnergyLaw(self)

    def help(self):

        print('{:20s} {:8s} {:10s}'.format('Long', 'Short', 'Value'))
        print('-'*20 + ' ' + '-'*8 + ' '+ '-'*10)

        for key, value in self.__dict__.items():

            if isinstance(value, (Tuple, Scalar)):
                print(f'{key:20s} {value.name:8s} {value.value}')

    def solve_linear_position_equation(self, unknown, axis='x'):

        return self.linear_position_equation.solve(unknown, axis)
    
    def solve_linear_velocity_equation(self, unknown, axis='x'):

        return self.linear_velocity_equation.solve(unknown, axis)

    def solve_newton_equation(self, unknown, axis='x'):

        return self.newton_equation.solve(unknown, axis)

    def solve_energy_equation(self, unknown):

        return self.energy_equation.solve(unknown)

    def set(self, parameter, value, axis=None):

        if not hasattr(self, parameter):
            raise ValueError(f'Parameter \'{parameter}\' not found')
        
        unknown = getattr(self, parameter)

        if isinstance(unknown, Tuple):
            unknown.define(value, axis=axis)
        else:
            unknown.define(value)

    def unset(self, parameter, axis=None):

        if not hasattr(self, parameter):
            raise ValueError(f'Parameter \'{parameter}\' not found')
        
        unknown = getattr(self, parameter)
        
        if isinstance(unknown, Tuple):
            unknown.undefine(axis=axis)
        else:
            unknown.undefine()

    def apply_force(self, name, value):

        force = Tuple(name, dimensions=self.dimensions, value=value)
        self.forces.append(force)

    def add_energy(self, name, value):

        energy = Scalar(name, value=value)
        self.energies.append(energy)