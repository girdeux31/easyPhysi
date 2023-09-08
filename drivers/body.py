from scipy.constants import electron_mass, proton_mass, neutron_mass, elementary_charge

from .scalar import Scalar
from .tuple import Tuple


class Body:

    def __init__(self, name, dimensions=2):

        if dimensions < 1 or dimensions > 3:
            raise ValueError('Parameter \'dimensions\' must be between 1 and 3')
        
        self.name = name
        self.dimensions = dimensions
        
        self.forces = list()
        self.energies = list()

        # initialize tuples
        
        self.initial_position = Tuple('p0', self.dimensions)
        self.initial_velocity = Tuple('v0', self.dimensions)
        self.position = Tuple('p', self.dimensions)
        self.velocity = Tuple('v', self.dimensions)
        self.gravity = Tuple('g', self.dimensions)
        self.acceleration = Tuple('a', self.dimensions)
        self.gravitational_force = Tuple('Fg', self.dimensions)
        self.gravitational_field_intensity = Tuple('gg', self.dimensions)  # this is the same as gravity 'g'
        self.electrical_force = Tuple('Fe', self.dimensions)
        self.electrical_field_intensity = Tuple('Ee', self.dimensions)

        # initialize scalars

        self.mass = Scalar('m')
        self.time = Scalar('t')
        self.charge = Scalar('q')
        self.gravitational_potential_energy = Scalar('Ug')
        self.gravitational_potential = Scalar('Vg')
        self.electrical_potential_energy = Scalar('Ue')
        self.electrical_potential = Scalar('Ve')

    def help(self):

        print('{:20s} {:8s} {:10s}'.format('Long', 'Short', 'Value'))
        print('-'*20 + ' ' + '-'*8 + ' '+ '-'*10)

        for key, value in self.__dict__.items():

            if isinstance(value, (Tuple, Scalar)):
                print(f'{key:20s} {value.name:8s} {value.value}')

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


electron = Body('electron')
electron.set('mass', electron_mass)
electron.set('charge', -elementary_charge)

proton = Body('proton')
proton.set('mass', proton_mass)
proton.set('charge', +elementary_charge)

neutron = Body('neutron')
neutron.set('mass', neutron_mass)
neutron.set('charge', 0.0)