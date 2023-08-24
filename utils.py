import math

from scipy.constants import electron_mass, proton_mass, neutron_mass, elementary_charge

none_type = type(None)


# electron = drivers.Body(name='electron')
# electron.set('mass', electron_mass)
# electron.set('charge', -elementary_charge)
# 
# proton = Body(name='proton')
# proton.set('mass', proton_mass)
# proton.set('charge', elementary_charge)
# 
# neutron = Body(name='neutron')
# neutron.set('mass', neutron_mass)
# neutron.set('charge', elementary_charge)

def magnitude(array):

    return math.sqrt(sum([x**2 for x in array]))

def distance(array_u, array_v):

    if len(array_u) != len(array_v):
        raise ValueError('Lengths of arrays mismatch')

    return math.sqrt(sum([(u-v)**2 for u, v in zip(array_u, array_v)]))

def inner_product(array_u, array_v):

    if len(array_u) != len(array_v):
        raise ValueError('Lengths of arrays mismatch')

    return sum([u*v for u, v in zip(array_u, array_v)])

def angle(array_u, array_v):

    if len(array_u) != len(array_v):
        raise ValueError('Lengths of arrays mismatch')
    
    return math.acos(inner_product(array_u, array_v)/magnitude(array_u)/magnitude(array_v))

def compare_floats(float_ref, float_test, decimals=2):
    
    power = round(math.log10(abs(float_ref))) if float_ref != 0.0 else 0.0
    power = power - decimals
    eps = 10**(power)

    return True if float_test - eps <= float_ref <= float_test + eps else False