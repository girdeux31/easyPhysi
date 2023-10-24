from scipy.constants import electron_mass, proton_mass, neutron_mass, elementary_charge

from .scalar import Scalar
from .vector import Vector


class Body:

    def __init__(self, name, dimensions=2):

        if dimensions < 1 or dimensions > 3:
            raise ValueError('Parameter \'dimensions\' must be between 1 and 3')
        
        self.name = name
        self.dimensions = dimensions
        
        self.forces = list()
        self.energies = list()

        # initialize parameters

        self.acceleration = Vector('a', self.dimensions)
        self.charge = Scalar('q')
        self.electrical_field_intensity = Vector('Ee', self.dimensions)
        self.electrical_force = Vector('Fe', self.dimensions)
        self.electrical_potential_energy = Scalar('Ue')
        self.electrical_potential = Scalar('Ve')
        self.gravitational_field_intensity = Vector('gg', self.dimensions)  # this is the same as gravity 'g'
        self.gravitational_force = Vector('Fg', self.dimensions)
        self.gravitational_potential_energy = Scalar('Ug')
        self.gravitational_potential = Scalar('Vg')
        self.gravity = Vector('g', self.dimensions)
        self.initial_position = Vector('p0', self.dimensions)
        self.initial_velocity = Vector('v0', self.dimensions)
        self.mass = Scalar('m')
        self.position = Vector('p', self.dimensions)
        self.time = Scalar('t')
        self.velocity = Vector('v', self.dimensions)

    def set(self, parameter, value, axis=None):

        if not hasattr(self, parameter):

            self.help()
            raise ValueError(f'Parameter \'{parameter}\' not found, see recognized parameters in table above')
        
        unknown = getattr(self, parameter)

        if isinstance(unknown, Vector):
            unknown.define(value, axis=axis)
        else:
            unknown.define(value)

    def unset(self, parameter, axis=None):

        if not hasattr(self, parameter):

            self.help()
            raise ValueError(f'Parameter \'{parameter}\' not found, see recognized parameters in table above')
        
        unknown = getattr(self, parameter)
        
        if isinstance(unknown, Vector):
            unknown.undefine(axis=axis)
        else:
            unknown.undefine()

    def apply_force(self, name, value):

        force = Vector(name, dimensions=self.dimensions, value=value)
        self.forces.append(force)

    def add_energy(self, name, value):

        energy = Scalar(name, value=value)
        self.energies.append(energy)

    def help(self):
        #TODO what about force and energy?

        print('The following parameters are recognized:')
        print('')
        print(' {:32s} {:8s} {:10s} {:16s}'.format('Parameter', 'Unknown', 'Type', 'Value'))
        print(' ' + '='*32 + ' ' + '='*8 + ' '+ '='*10 + ' '+ '='*16)

        for key, value in self.__dict__.items():

            if isinstance(value, (Vector, Scalar)):
                print(f' {key:32s} {value.name:8s} {type(value).__name__:10s} {value.value}')

        print('')


electron = Body('electron')
electron.set('mass', electron_mass)
electron.set('charge', -elementary_charge)

proton = Body('proton')
proton.set('mass', proton_mass)
proton.set('charge', +elementary_charge)

neutron = Body('neutron')
neutron.set('mass', neutron_mass)
neutron.set('charge', 0.0)