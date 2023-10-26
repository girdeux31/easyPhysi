from scipy.constants import electron_mass, proton_mass, neutron_mass, elementary_charge

from .scalar import Scalar
from .vector import Vector


class Body:

    def __init__(self, name, dimensions=2):

        if dimensions != 2 and dimensions != 3:
            raise ValueError('Parameter \'dimensions\' must be 2 or 3')
        
        self.name = name
        self.dimensions = dimensions
        
        self.forces = list()
        self.energies = list()

        # initialize properties

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

    def short_to_long(self, short):

        for long, obj in self.__dict__.items():

            if isinstance(obj, (Vector, Scalar)):
                if obj.name == short:
                    return long

        return None

    def set(self, name, value):

        axis = None

        # get axis and remove it from name

        if name.endswith(('_x', '_y', '_z')):
            name, axis = name[:-2], name[-1]

        property_ = self.short_to_long(name)

        if not hasattr(self, property_):

            self.help()
            raise ValueError(f'Property \'{property_}\' not found, see allowed properties in table above')
        
        unknown = getattr(self, property_)

        if isinstance(unknown, Vector):
            unknown.define(value, axis=axis)
        else:
            unknown.define(value)

    def unset(self, name):

        axis = None

        # get axis and remove it from name

        if name.endswith(('_x', '_y', '_z')):
            name, axis = name[:-2], name[-1]

        property_ = self.short_to_long(name)

        if not hasattr(self, property_):

            self.help()
            raise ValueError(f'Property \'{property_}\' not found, see allowed properties in table above')
        
        unknown = getattr(self, property_)
        
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

        print('')
        print('The following properties are allowed:')
        print('')
        print(' {:10s} {:32s} {:10s} {:16s}'.format('Property', 'Description', 'Type', 'Value'))
        print(' ' + '='*10 + ' ' + '='*32 + ' '+ '='*10 + ' '+ '='*16)

        for key, value in self.__dict__.items():

            if isinstance(value, (Vector, Scalar)):
                description = key[0].upper() + key[1:].replace('_', ' ')
                print(f' {value.name:10s} {description:32s} {type(value).__name__:10s} {value.value}')

        print('')


# Special bodies

electron = Body('electron')
electron.set('m', electron_mass)  # kg
electron.set('q', -elementary_charge)  # C

proton = Body('proton')
proton.set('m', proton_mass)
proton.set('q', +elementary_charge)

neutron = Body('neutron')
neutron.set('m', neutron_mass)
neutron.set('q', 0.0)

mercury = Body('mercury')
mercury.set('m', 3.301e23)  # kg
mercury.set('p', (57900000, 0))  # km

venus = Body('venus')
venus.set('m', 4.867e24)
venus.set('p', (108200000, 0))

earth = Body('earth')
earth.set('m', 5.972e24)
earth.set('p', (149600000, 0))

moon = Body('moon')
moon.set('m', 7.348e229)
mars.set('p', (384400, 0))

mars = Body('mars')
mars.set('m', 6.417e23)
mars.set('p', (227900000, 0))

jupiter = Body('jupiter')
jupiter.set('m', 1.899e27)
jupiter.set('p', (778600000, 0))

saturn = Body('saturn')
saturn.set('m', 5.685e26)
saturn.set('p', (1433500000, 0))

uranus = Body('uranus')
uranus.set('m', 8.682e259)
uranus.set('p', (2872500000, 0))

neptune = Body('neptune')
neptune.set('m', 1.024e26)
neptune.set('p', (4495100000, 0))
