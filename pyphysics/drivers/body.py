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

        # initialize parameters

        self.acceleration = Tuple('a', self.dimensions)
        self.charge = Scalar('q')
        self.electrical_field_intensity = Tuple('Ee', self.dimensions)
        self.electrical_force = Tuple('Fe', self.dimensions)
        self.electrical_potential_energy = Scalar('Ue')
        self.electrical_potential = Scalar('Ve')
        self.gravitational_field_intensity = Tuple('gg', self.dimensions)  # this is the same as gravity 'g'
        self.gravitational_force = Tuple('Fg', self.dimensions)
        self.gravitational_potential_energy = Scalar('Ug')
        self.gravitational_potential = Scalar('Vg')
        self.gravity = Tuple('g', self.dimensions)
        self.initial_position = Tuple('p0', self.dimensions)
        self.initial_velocity = Tuple('v0', self.dimensions)
        self.mass = Scalar('m')
        self.position = Tuple('p', self.dimensions)
        self.time = Scalar('t')
        self.velocity = Tuple('v', self.dimensions)

    def set(self, parameter, value, axis=None):

        if not hasattr(self, parameter):

            self.help()
            raise ValueError(f'Parameter \'{parameter}\' not found, see recognized parameters in table above')
        
        unknown = getattr(self, parameter)

        if isinstance(unknown, Tuple):
            unknown.define(value, axis=axis)
        else:
            unknown.define(value)

    def unset(self, parameter, axis=None):

        if not hasattr(self, parameter):

            self.help()
            raise ValueError(f'Parameter \'{parameter}\' not found, see recognized parameters in table above')
        
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

    def help(self):
        #TODO what about force and energy?

        print('The following parameters are recognized:')
        print('')
        print(' {:32s} {:8s} {:10s} {:16s}'.format('Parameter', 'Unknown', 'Type', 'Value'))
        print(' ' + '='*32 + ' ' + '='*8 + ' '+ '='*10 + ' '+ '='*16)

        for key, value in self.__dict__.items():

            if isinstance(value, (Tuple, Scalar)):
                print(f' {key:32s} {value.name:8s} {type(value).__name__:10s} {value.value}')

        print('')

    # def help(self):

    #     print('The following parameters are recognized:')
    #     print('')
    #     print('Parameter                        Unknown Type')
    #     print('================================ ======= ======')
    #     print('acceleration                     a       tuple')
    #     print('charge                           q       scalar')
    #     print('electrical_field_intensity       Ee      tuple')
    #     print('electrical_force                 Fe      tuple')
    #     print('electrical_potential             Ve      scalar')
    #     print('electrical_potential_energy      Ue      scalar')
    #     print('gravitational_field_intensity    gg      tuple')  # this is the same as gravity 'g'
    #     print('gravitational_force              Fg      tuple')
    #     print('gravitational_potential          Vg      scalar')
    #     print('gravitational_potential_energy   Ug      scalar')
    #     print('gravity                          g       tuple')
    #     print('initial_position                 p0      tuple')
    #     print('initial_velocity                 v0      tuple')
    #     print('mass                             m       scalar')
    #     print('position                         p       tuple')
    #     print('time                             t       scalar')
    #     print('velocity                         v       tuple')
    #     print('')


electron = Body('electron')
electron.set('mass', electron_mass)
electron.set('charge', -elementary_charge)

proton = Body('proton')
proton.set('mass', proton_mass)
proton.set('charge', +elementary_charge)

neutron = Body('neutron')
neutron.set('mass', neutron_mass)
neutron.set('charge', 0.0)