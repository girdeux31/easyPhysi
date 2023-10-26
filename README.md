# pyPhysics

pyPhysics is a physics library to solve pre-universitary physics problems. The physics areas that are covered are:

 - Kinematics
 - Dinamics
 - Energy conservation
 - Gravitational field
 - Electrical field
 
See examples for all of them in Section XXX.

## Characteristics

 - Program: pyPhysics
 - Version: 1.0
 - Author: Carles Mesado
 - Date: 31/10/2023
 - Size: ~ 18 KiB
 
## Requirements

Python 3.10 and the following third-party modules:

 - matplotlib>=3.7.0
 - scipy>=1.11.0
 - sympy==1.12

## Installation

``pip install pyphysics``

## Usage

### Main structure

Most pre-university physics problems can be solved following this structure composed of a few lines.

```
from pyphysics.drivers.universe import Universe
from pyphysics.drivers.body import Body


universe = Universe(dimensions=2)  # 2 o 3 dimensions

body = Body('my_body', dimensions=2)
body.set('my_param', value)

# define more properties or more bodies as needed

universe.add_body(body)

# add more bodies as needed

unknown = universe.physics_equation('my_body').solve('my_unknown')
```

Let's take the code apart line by line. 

 - Line 1 and 2: import `Universe` and `Body`, objects that are needed in every single problem solved with this library.
 - Line 5: define a universe instance with `Universe` class and include the dimensions of it, only 2 o 3 dimensions are allowed.
 - Line 7: define a body instance with `Body` class, we include its name and dimensions. Define as many bodies as needed provided that they have different names.
 - Line 8: define a property for the body created in previous line, property name and value. See a list of allowed properties in [Section](#properties). Define as many properties as needed provided they are listed in Section \@ref(sec:properties) and follow its type, see Section \@ref(sec:property_types).
 - Line 12: add all defined bodies to the universe.
 - Line 16: solve the physics equation over a specific body and define the unknown(s). See a list of allowed equations in Section XXX.

### <a name="properties"></a>Properties

The following properties can be defined in any body.

 |Properties                      |Unknown |Type      |  Value   	|
 |--------------------------------|--------|----------|-------------|
 |acceleration                    |a       |Vector    |(a_x, a_y)	|
 |charge                          |q       |Scalar    |q			|
 |electrical_field_intensity      |Ee      |Vector    |(Ee_x, Ee_y)	|
 |electrical_force                |Fe      |Vector    |(Fe_x, Fe_y)	|
 |electrical_potential_energy     |Ue      |Scalar    |Ue			|
 |electrical_potential            |Ve      |Scalar    |Ve			|
 |gravitational_field_intensity   |gg      |Vector    |(gg_x, gg_y)	|
 |gravitational_force             |Fg      |Vector    |(Fg_x, Fg_y)	|
 |gravitational_potential_energy  |Ug      |Scalar    |Ug			|
 |gravitational_potential         |Vg      |Scalar    |Vg			|
 |gravity                         |g       |Vector    |(g_x, g_y)	|
 |initial_position                |p0      |Vector    |(p0_x, p0_y)	|
 |initial_velocity                |v0      |Vector    |(v0_x, v0_y)	|
 |mass                            |m       |Scalar    |m			|
 |position                        |p       |Vector    |(p_x, p_y)	|
 |time                            |t       |Scalar    |t			|
 |velocity                        |v       |Vector    |(v_x, v_y)	|
 
Use `set` method in a body instance to define a parameter in a body and define its value according to its type. See value types in Section XXX.

`body.set('my_param', value)`

### Parameter types

There are two types of parameters: scalars (`mass` for instance) and vectors (`gravity` for instance).

#### Scalars

They are integers of floats, examples follow.

```
body.set('mass', 250)       # int
body.set('charge', 5.0E-9)  # float
```

#### Vectors

They are list or tuples, examples follow.

```
body.set('gravity', [0.0, -9.81])  # list
body.set('position', (0, +3))      # tuple
```

The length of `value` (components) must be the same as defined in the instance of universe.

It is also possible to define only one component in a vector parameter (the other may be irrelevant or unknown). To do so, just include the optional parameter `axis` with its axis component `x`, `y` or `z`.

```
body.set('position', 0, axis='x')
```

### Equations

The following equations can be solved.

 |Equation                                |Type      |Parameters      |
 |----------------------------------------|----------|--------------- |
 |electrical_field_intensity_equation     |Vectorial |Ee, p, q        |
 |electrical_force_equation               |Vectorial |Fe, p, q        |
 |electrical_potential_energy_equation    |Scalar    |Ue, p, q        |
 |electrical_potential_equation           |Scalar    |Ve, p, q        |
 |energy_equation                         |Scalar    |E 		      |
 |gravitational_field_intensity_equation  |Vectorial |gg, m, p        |
 |gravitational_force_equation            |Vectorial |Fg, m, p        |
 |gravitational_potential_energy_equation |Scalar    |Ug, m, p        |
 |gravitational_potential_equation        |Scalar    |Vg, m, p        |
 |linear_position_equation                |Vectorial |g, p, p0, t, v0 |
 |linear_velocity_equation                |Vectorial |g, t, v, v0 	  |
 |newton_equation                         |Vectorial |F, a, m 		  |
 
Use any above equation in an instance of a universe and include the body the equation will be applied to. Then use the `solve` method and include the unknown(s) to be solved, see third column in above table.

`universe.physics_equation('my_body').solve('my_unknown')`

Units are up to the user. SI is recommended but other systems can be used provided that different units are consistent.

### Equation types

There are two types of equations: scalar (`energy_equation` for instance) and vectorial (`newton_equation` for instance).

#### Scalar

Only one input/output unknown is accepted.

```
vf = universe.energy_equation('body').solve('vf')
```

#### Vectorial

As many input/output unknowns as dimensions defined in the instance of universe are accepted. Specific vector component must be append to input unknowns, such as `a_x` and `a_y` for acceleration, see forth column in Table XXX. No name restriction apply for output unkonowns.

```
a_x, a_y = universe.newton_equation('body').solve(['a_x', 'a_y'])
```

### Other features

## Examples

### Kinematics

#### K-1

**Technical description**

**Statement**

**Code**

**Result**

### Dinamics

#### D-1

### Energy conservation

#### EC-1

### Gravitational field

#### GF-1

### Electrical field

#### EF-1

## Bugs

 - 
   
## License

This project includes MIT License. A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

## Contact

Visit GitHub page at https://github.com/girdeux31/pyPhysics

Feel free to contact mesado31@gmail.com for any suggestion or bug.
     
