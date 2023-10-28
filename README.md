# <a name="sec:top"></a>pyPhysics

> [!WARNING]
> **Library under development yet**

pyPhysics is a physics library to solve pre-universitary physics problems. The physics areas that are covered in the library, along with some examples, are summarized in the following [table](#tab:areas).

<a name="tab:areas"></a>

 | Area                 | Examples                                          |
 |----------------------|---------------------------------------------------|
 | Kinematics           | [K-examples](#sec:example-kinematics)             |
 | Dinamics             | [D-examples](#sec:example-dinamics)               |
 | Energy conservation  | [EC-examples](#sec:example-energy-conservation)   |
 | Gravitational field  | [GF-examples](#sec:example-gravitational-field)   |
 | Electrical field     | [EF-examples](#sec:example-electrical-field)      |

## <a name="sec:index"></a>Index

1. [Characteristics](#sec:characteristics)
2. [Requirements](#sec:requirementes)
3. [Installation](#sec:installation)
4. [Usage](#sec:usage)
    1. [Main structure](#sec:main-structure)
    2. [Properties](#sec:properties)
    3. [Special bodies](#sec:special-bodies)
    4. [Equations](#sec:equations)
    5. [Advance features](#sec:advance-features)
5. [Examples](#sec:examples)
    1. [Kinematics](#sec:example-kinematics)
    2. [Dinamics](#sec:example-dinamics)
    3. [Energy conservation](#sec:example-energy-conservation)
    4. [Gravitational field](#sec:example-gravitational-field)
    5. [Electrical field](#sec:example-electrical-field)
6. [Bugs and limitations](#sec:bugs-limitations)
7. [License](#sec:licence)
8. [Contact](#sec:contact)

## <a name="sec:characteristics"></a>Characteristics

<a name="tab:characteristics"></a>

 | Characteristic   | Value         |
 |------------------|---------------|
 | Program          | pyPhysics     |
 | Version          | 1.0           |
 | Author           | Carles Mesado |
 | Date             | 31/10/2023    |
 | Size             | ~ 18 KiB      |
 
## <a name="sec:requirementes"></a>Requirements

Python 3.10 and the following third-party modules:

 - matplotlib>=3.7.0
 - scipy>=1.11.0
 - sympy==1.12

## <a name="sec:installation"></a>Installation

> [!WARNING]
> **Package not in pypi yet**

Install the package with pip,

`pip install pyphysics`

or clone the GitHub repository.

`gh repo clone girdeux31/pyPhysics`

## <a name="sec:usage"></a>Usage

### <a name="sec:main-structure"></a>Main structure

Most pre-university physics problems can be solved following this structure composed of a few lines.

```
from pyphysics.drivers.universe import Universe
from pyphysics.drivers.body import Body

universe = Universe(dimensions=2)  # 2 o 3 dimensions

body = Body('my_body', dimensions=2)
body.set('my_prop', value)

# define more properties or more bodies as needed

universe.add_body(body)

# add more bodies as needed

unknown = universe.physics_equation('my_body').solve('my_unknown')
```

Let's take the code apart line by line. 

 - Line 1 and 2: import `Universe` and `Body`, objects that are needed in every single problem solved with this library.
 - Line 5: define a universe instance with `Universe` class and include the dimensions of it, only 2 o 3 dimensions are allowed.
 - Line 7: define a body instance with `Body` class, we include its name and dimensions. Define as many bodies as needed provided that they have different names.
 - Line 8: define a property for the body instanciated in previous line and its value. Define as many properties as needed provided they are listed in [Table](#tab:properties). Properties must fulfill its type, see [Section](#sec:property-types).
 - Line 12: add all defined bodies to the universe.
 - Line 16: solve the physics equation over a specific body and define the unknown(s). See a list of allowed equations in [Table](#tab:equations).

### <a name="sec:properties"></a>Properties

The following properties can be defined in any body.

> [!NOTE]
> Property names are case sensitive.

<a name="tab:properties"></a>

 |Property |Description                     |Type      |Components    |           
 |---------|--------------------------------|----------|--------------|
 |a        |Acceleration                    |Vector    |(a_x, a_y)    |
 |q        |Charge                          |Scalar    |q             |
 |Ee       |Electrical field intensity      |Vector    |(Ee_x, Ee_y)  |
 |Fe       |Electrical force                |Vector    |(Fe_x, Fe_y)  |
 |Ue       |Electrical potential energy     |Scalar    |Ue            |
 |Ve       |Electrical potential            |Scalar    |Ve            |
 |gg       |Gravitational field intensity   |Vector    |(gg_x, gg_y)  |
 |Fg       |Gravitational force             |Vector    |(Fg_x, Fg_y)  |
 |Ug       |Gravitational potential energy  |Scalar    |Ug            |
 |Vg       |Gravitational potential         |Scalar    |Vg            |
 |g        |Gravity                         |Vector    |(g_x, g_y)    |
 |p0       |Initial position                |Vector    |(p0_x, p0_y)  |
 |v0       |Initial velocity                |Vector    |(v0_x, v0_y)  |
 |m        |Mass                            |Scalar    |m             |
 |p        |Position                        |Vector    |(p_x, p_y)    |
 |t        |Time                            |Scalar    |t             |
 |v        |Velocity                        |Vector    |(v_x, v_y)    |
 
Use `set` method in an instanciated body to define its property and define its value according to its type. See value types in [Section](#sec:property-types).

> [!NOTE]
> Units are up to the user. Eventhough SI is recommended, other systems can be used provided that different units are consistent.

> [!NOTE]
> Force and energy cannot be defined as properties, see [Section](#sec:XXX)

#### <a name="sec:property-types"></a>Property types

There are two types of properties: **scalars** (`m` for mass) and **vectors** (`g` for gravity).

##### <a name="sec:property-type-scalar"></a>Scalars

They are integers of floats, examples follow.

```
body.set('prop', 250)       # int
body.set('prop', 5.0E-9)    # float
```

##### <a name="sec:property-type-vectors"></a>Vectors

They are list or tuples, examples follow.

```
body.set('prop', [0.0, -9.81])  # list
body.set('prop', (0, +3))       # tuple
```

The length of `value` (components) must be the same as defined in the instance of universe.

> [!NOTE]
> It is also possible to define only one component in a vector parameter (the other may be irrelevant or unknown). To do so, append `_x`, `_y` or `_z` to the property name according to the desired axis.

```
body.set('prop_x', value_x)
body.set('prop_y', value_y)
body.set('prop_z', value_z)
```

#### <a name="sec:property-nondefined"></a>Non-defined properties

Force (mainly used in `newton_equation`) and energy (mainly used in `energy_conservation_equation`) cannot be defined as properties in an instanciated body with `set` method. Instead they are defined in an instanciated body with `apply_force` and `add_energy` methods respectively.

```
body.apply_force('my_force', value)
body.add_energy('my_energy', value)
```

This is designed on purpose because many different forces and energies can be applied/added to a body and they have different algebraical expressions. Thus, the algebraic expression for the force and energy must be defined by the user.

See examples for Newton equation and energy conservation equation in [D-examples](#sec:example-dinamics) and [E-examples](#sec:example-energy-conservation) respectively.

### <a name="sec:special-bodies"></a>Special bodies

Special bodies are pre-defined to be used. There are two types: particles and celestial bodies.

`# TODO tables`

 - Particles: `electron`, `proton`, `neutron`
 - Celestial bodies: `sun`, `mercury`, `venus`, `earth`, `moon`, `mars`, `jupiter`, `saturn`, `uranus`, `neptune`

`from pyphysics.drivers.body import special_body`

See example in [EF-examples](#sec:example-electrical-field).
 
### <a name="sec:equations"></a>Equations

The following equations can be solved.

> [!NOTE]
> Equation names are case sensitive.

<p style="text-align: center;"><a name="tab:equations"></a>Equations allowed for universe</p>

 |Equation                                |Type      |Properties      |
 |----------------------------------------|----------|--------------- |
 |electrical_field_intensity_equation     |Vectorial |Ee, p, q        |
 |electrical_force_equation               |Vectorial |Fe, p, q        |
 |electrical_potential_energy_equation    |Scalar    |Ue, p, q        |
 |electrical_potential_equation           |Scalar    |Ve, p, q        |
 |energy_conservation_equation            |Scalar    |E 		      |
 |gravitational_field_intensity_equation  |Vectorial |gg, m, p        |
 |gravitational_force_equation            |Vectorial |Fg, m, p        |
 |gravitational_potential_energy_equation |Scalar    |Ug, m, p        |
 |gravitational_potential_equation        |Scalar    |Vg, m, p        |
 |linear_position_equation                |Vectorial |g, p, p0, t, v0 |
 |linear_velocity_equation                |Vectorial |g, t, v, v0 	  |
 |newton_equation                         |Vectorial |F, a, m 		  |
 
Use any above equation in an instance of a universe and include the body the equation will be applied to. Then use the `solve` method and include the unknown(s) to be solved, see third column in above table.

`universe.physics_equation('my_body').solve('my_unknown')`

#### <a name="sec:equation-types"></a>Equation types

There are two types of equations: scalar (`energy_conservation_equation` for instance) and vectorial (`newton_equation` for instance).

##### <a name="sec:equation-type-scalar"></a>Scalar

Only one input/output unknown is accepted.

```
out = universe.physics_equation('my_body').solve('my_unk')
```

##### <a name="sec:equation-type-vectorial"></a>Vectorial

As many input and output unknowns as universe dimensions defined are accepted. Vector component must be append to input unknown names, such as `a_x` and `a_y` for acceleration, see forth column in [Table](#tab:properties). No name restriction apply for output unkonowns.

```
out_x, out_y = universe.physics_equation('my_body').solve(['unk_x', 'unk_y'])
```

### <a name="sec:advance-features"></a>Advance features

Library most useful features are already defined. However, for the sake of completeness, a few more features for the advance user are defined in this section.

`# TODO get_equation`
`# TODO first_positive_root`

#### <a name="sec:other-feature-magnitude"></a>Vector module

Vectorial equations give vectorial results as vector components. A function is available to obtain its module or _magnitude_. See example in [example XX](#sec:).

```
from pyphysics.utils import magnitude
prop = magnitude((prop_x, prop_y))
```

#### <a name="sec:other-feature-functions"></a>Working with functions

Equations return numerical values if there is only one unknown, but return functions if there is more than one unknown. Then, \'subs\' method can be used to replace an unknown by a specified numerical value. See example in [example XX](#sec:).

```
foo = universe.physics_equation('body').solve('my_unk')
out = foo.subs('my_sym', value)
```

#### <a name="sec:other-feature-systems"></a>Solving system of equations

System of equations can be defined -with `System` class- and solved with `solve` method. The `solve` method accepts a list with as many unknowns as equations defined in the system. See example in [example XX](#sec:).

```
system = System()
system.add_equation(equation)

# add as meny equations as needed

x, y, z = system.solve(['x', 'y', 'z'])
```

#### <a name="sec:other-feature-plot"></a>Plotting equations

Method `plot` can be used over any equation to plot unknowns in the form of function `independent = f(dependent)`.

`universe.physics_equation('my_body').plot(independent, dependent, x_range, points=100, path=None, show=True)`

Arguments are described hereafter.

 - `independent`: if equation is [scalar](#sec:equation-type-scalar), then only one independent unknown is expected. If equation is [vectorial](#sec:equation-type-vectorial), then exactly the same number of universe dimensions are expected as independent unknowns (as a list). See examples below.
 - `dependent`: exactle one unknown is expected.
 - `x_range`: range to plot for dependent unknown (x-axis).
 - `points`: number of points to plot, optional argument, default is 100.
 - `path`: path to save image as file, optional argument, by default it is not saved.
 - `show`: if `True` the plot is shown on screen, optional argument, by default it is `True`.

See examples for scalar equation in [example XX](#sec:) and vectorial equation in [example XX](#sec:).

## <a name="sec:examples"></a>Examples

### <a name="sec:example-kinematics"></a>Kinematics

#### <a name="sec:example-k1"></a>Example K-1


## <a name="sec:bugs-limitations"></a>Bugs and limitations

`# TODO Limitation with p being the unknown`

## <a name="sec:licence"></a>License

This project includes MIT License. A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

## <a name="sec:contact"></a>Contact

Feel free to contact mesado31@gmail.com for any suggestion or bug.

> [!IMPORTANT]
> Visit GitHub page at https://github.com/girdeux31/pyPhysics
