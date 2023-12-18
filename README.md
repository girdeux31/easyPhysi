# <a name="sec-top"></a>pyPhysics

> [!WARNING]
> **Library under development yet**

pyPhysics is a physics library to solve pre-universitary physics problems. The physics areas that are covered by pyPhisics are summarized hereafter. See the [main structure](#sec-main-structure) to use pyPhysics and also some [examples](#sec-examples).

 - Kinematics
 - Dynamics
 - Energy conservation
 - Gravitational field
 - Electrical field

The main characteristics for pyPhysics are summarized in the following table.

<a name="tab-characteristics"></a>

 | Characteristic   | Value         |
 |------------------|---------------|
 | Name             | pyPhysics     |
 | Version          | 1.0           |
 | Author           | Carles Mesado |
 | Date             | 31/10/2023    |
 | Size             | ~ 18 KiB      |

## <a name="sec-index"></a>Index

1. [Installation](#sec-installation)
2. [Usage](#sec-usage)
    1. [Main structure](#sec-main-structure)
    2. [Properties](#sec-properties)
    3. [Special bodies](#sec-special-bodies)
    4. [Equations](#sec-equations)
    5. [Advance features](#sec-advance-features)
3. [Examples](#sec-examples)
    1. [Kinematics](#sec-example-kinematics)
    2. [Dynamics](#sec-example-dynamics)
    3. [Energy conservation](#sec-example-energy-conservation)
    4. [Gravitational field](#sec-example-gravitational-field)
    5. [Electrical field](#sec-example-electrical-field)
4. [Bugs and limitations](#sec-bugs-limitations)
5. [License](#sec-licence)
6. [Contact](#sec-contact)

## <a name="sec-installation"></a>Installation

> [!WARNING]
> **Package not in pypi yet**

> [!NOTE]
> pyPhysics is developed and tested with Python 3.10.

Install the package with pip,

`pip install pyphysics`

or clone the GitHub repository.

`gh repo clone girdeux31/pyPhysics`

The following third-party modules are requirements.

 - matplotlib>=3.7.0
 - scipy>=1.11.0
 - sympy==1.12

## <a name="sec-usage"></a>Usage

### <a name="sec-main-structure"></a>Main structure

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

 - Line 1 and 2: import `Universe` and `Body` objects, these are needed in every single problem solved with this library.
 - Line 4: define a universe instance with `Universe` class and include the dimensions of it, only 2 o 3 dimensions are allowed.
 - Line 6: define a body instance with `Body` class, its name and dimensions are included as arguments. Define as many bodies as needed provided that they have different names.
 - Line 7: define a property for the body instanciated in previous line and its value. Define as many properties as needed provided they are listed in [Table](#tab-properties). Properties must fulfill its type, see [Section](#sec-property-types).
 - Line 11: add all defined bodies to the universe.
 - Line 15: solve the physics equation over a specific body and define the unknown(s). See a list of allowed equations and unknowns in [Table](#tab-equations).

### <a name="sec-properties"></a>Properties

The following properties can be defined in any body.

> [!NOTE]
> Property names are case sensitive.

<a name="tab-properties"></a>

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
 
Use `set` method in an instanciated body to define its property and define its value according to its type. See value types in [Section](#sec-property-types).

> [!NOTE]
> Units are up to the user. Eventhough SI is recommended, other systems can be used provided that different units are consistent.

> [!NOTE]
> Force and energy cannot be defined as properties since each force and energy is defined by its own formula, see [Section](#sec-property-nondefined).

#### <a name="sec-property-types"></a>Property types

There are two types of properties: **scalars** (for example `m` for mass) and **vectors** (for example `g` for gravity).

##### <a name="sec-property-type-scalar"></a>Scalars

They are integers of floats, examples follow.

```
body.set('prop', 250)       # int
body.set('prop', 5.0E-9)    # float
```

##### <a name="sec-property-type-vectors"></a>Vectors

They are list or tuples (either integers or floats), examples follow.

```
body.set('prop', [0.0, -9.81])  # list
body.set('prop', (0, +3))       # tuple
```

The length of `value` (components) must be the same as defined in the instance of the body the property applies to and also to the instance of universe.

> [!NOTE]
> It is also possible to define only one component in a vector parameter (the other may be irrelevant or unknown). To do so, append `_x`, `_y` or `_z` to the property name according to the desired axis.

```
body.set('prop_x', value_x)
body.set('prop_y', value_y)
body.set('prop_z', value_z)
```

#### <a name="sec-property-nondefined"></a>Non-defined properties

Force (mainly used in `newton_equation`) and energy (mainly used in `energy_conservation_equation`) cannot be defined as properties in an instanciated body with `set` method (note that they are not listed in [Table](#tab-equations)). Instead they can be defined in an instanciated body with `apply_force` and `add_energy` methods respectively.

```
body.apply_force('my_force', value)
body.add_energy('my_energy', value)
```

This is designed on purpose because many different forces and energies can be applied/added to a body and they have different algebraic expressions. Thus, the algebraic expression for the force and energy must be defined by the user.

See examples for Newton equation and energy conservation equation in [Dynamic Examples](#sec-example-dynamics) and [Energy Conservation Examples](#sec-example-energy-conservation) respectively.

### <a name="sec-special-bodies"></a>Special bodies

Special bodies are pre-defined bodies that are ready to be used. There are two types of special bodies: subatomic particles and celestial bodies, see following tables. The mass and charge of subatomic particles are defined in kilograms and coulombs. The mass and position of celestial bodies are defined in kilograms and kilometers.

<a name="tab-body-particles"></a>

| Body     | Mass (kg) | Charge (C) |
|----------|-----------|------------|
| electron | 9.109e-31 | -1.602e-19 |
| proton   | 1.673e-27 | 1.602e-19  |
| neutron  | 1.675e-27 | 0.0        |

> [!NOTE]
> The distance of celestial bodies is the average distance to the sun (except for the moon, which is the average distance to the Earth) and is defined in the x-axis.

<a name="tab-body-celestial"></a>

| Body     | Mass (kg) | Position (km) |
|----------|-----------|---------------|
| sun      | 1.988e30  | 0.0           |
| mercury  | 3.301e23  | 57900000      |
| venus    | 4.867e24  | 108200000     |
| earth    | 5.972e24  | 149600000     |
| moon     | 7.348e22  | 384400        |
| mars     | 6.417e23  | 227900000     |
| jupiter  | 1.899e27  | 778600000     |
| saturn   | 5.685e26  | 1433500000    |
| uranus   | 8.682e25  | 2872500000    |
| neptune  | 1.024e26  | 4495100000    |

Import them using the following line and use them without instanciating the body or defining its main properties, see [Electrical Field Examples](#sec-example-ef2).

`from pyphysics.drivers.body import special_body`
 
### <a name="sec-equations"></a>Equations

The following equations can be solved. Each equation is a method defined in the `Universe` class.

> [!NOTE]
> Equation names are case sensitive.

<a name="tab-equations"></a>

 |Equation                                |Type      |Unknowns        |
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
 
Use any above equation in an instance of universe and include the body the equation applies to. Then use the `solve` method and include the unknown(s) to be solved, see third column in above table.

`universe.physics_equation('my_body').solve('my_unknown')`

#### <a name="sec-equation-types"></a>Equation types

There are two types of equations: scalar (for example `energy_conservation_equation`) and vectorial (for example `newton_equation`).

##### <a name="sec-equation-type-scalar"></a>Scalar

Only one unknown is accepted.

```
out = universe.physics_equation('my_body').solve('my_unk')
```

##### <a name="sec-equation-type-vectorial"></a>Vectorial

As many unknowns as universe dimensions are accepted, these must be defined as a list and passed as argument of `solve` method. Vector components must be append to unknown names, such as `a_x` and `a_y` for acceleration, see [Section](#sec-property-type-vectors) and forth column in [Table](#tab-properties). The same number of unknowns must be defined as outputs, no name restriction apply for output unknowns.

```
out_x, out_y = universe.physics_equation('my_body').solve(['unk_x', 'unk_y'])
```

### <a name="sec-advance-features"></a>Advance features

The most useful features are already defined. However, for the sake of completeness, a few more features for the advance user are defined in this section.

`# TODO get_equation`
`# TODO first_positive_root`

#### <a name="sec-other-feature-magnitude"></a>Vector module

Vectorial equations give results as vector components. A function is available to obtain its module or _magnitude_, see [Example](#sec-example-k1).

```
from pyphysics.utils import magnitude
prop = magnitude((prop_x, prop_y))
```

#### <a name="sec-other-feature-functions"></a>Working with functions

Equations return numerical values if there is only one unknown (all properties are defined but one), but return functions if there is more than one unknown (two or more properties are left undefined). Use \'subs\' method to replace an unknown by a specified numerical value, see [Example](#sec-example-d1).

```
foo = universe.physics_equation('body').solve('my_unk')
out = foo.subs('my_sym', value)
```

#### <a name="sec-other-feature-systems"></a>Solving system of equations

System of equations can be defined -with `System` class- and solved with `solve` method. The `solve` method accepts a list with as many unknowns as equations defined in the system, see [example XX](#sec-example-d2).

```
equation = universe.physics_equation('body').solve('my_unk')
system = System()
system.add_equation(equation)

# define and add as meny equations as needed

x, y, z = system.solve(['x', 'y', 'z'])
```

#### <a name="sec-other-feature-plot"></a>Plotting equations

Method `plot` can be used over any equation to plot unknowns in the form of function `independent = f(dependent)`.

`universe.physics_equation('my_body').plot(independent, dependent, x_range, points=100, path=None, show=True)`

Arguments are described hereafter.

 - `independent`: if equation is [scalar](#sec-equation-type-scalar), then only one independent unknown is expected. If equation is [vectorial](#sec-equation-type-vectorial), then exactly the same number of universe dimensions are expected as independent unknowns (as a list). See examples below.
 - `dependent`: exactle one unknown is expected.
 - `x_range`: range to plot for dependent unknown (x-axis).
 - `points`: number of points to plot, optional argument, default is 100.
 - `path`: path to save image as file, optional argument, by default it is None and no image is saved.
 - `show`: if `True` the plot is shown on screen, optional argument, by default it is `True`.

See a plot for scalar equation in [Example](#sec-example-ec2).

## <a name="sec-examples"></a>Examples

### <a name="sec-example-kinematics"></a>Kinematics

#### <a name="sec-example-k1"></a>Example K-1

URL: https://fq.iespm.es/documentos/janavarro/fisica2bach/T0_vectores_cinematica.pdf

Problem: 10

Statement: A ball falls from a roof located 10 m high, forming a 30º angle with the horizontal, with a speed of 2 m/s. Calculate:

a) At what distance from the wall does it hit the ground?

b) The speed it has when it reaches the ground (disregard air friction).

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.utils import magnitude

alpha = math.radians(-30)
g = (0.0, -9.81)
p0 = (0.0, 10.0)
v0 = (2.0*math.cos(alpha), 2.0*math.sin(alpha))
py = 0.0

body = Body('body', dimensions=2)

body.set('g', g)
body.set('p0', p0)
body.set('v0', v0)
body.set('p_y', py)

universe = Universe()
universe.add_body(body)

t = universe.linear_position_equation('body').get_equation('y').solve('t', first_positive_root=True)

body.set('t', t)

p_x = universe.linear_position_equation('body').get_equation('x').solve('p_x', first_positive_root=True)

v_x, v_y = universe.linear_velocity_equation('body').solve(['v_x', 'v_y'])
v = magnitude((v_x, v_y))
```

Solution:

```
p_x = 2.30 m
v = 14.15 m/s
```

### <a name="sec-example-dynamics"></a>Dynamics

#### <a name="sec-example-d1"></a>Example D-1

URL: https://fq.iespm.es/documentos/rafael_artacho/4_ESO/08.%20Problemas%20Las%20fuerzas.pdf

Problem: 14

Statement: The following ramp has an inclination of 25º. Determine the force that must be exerted on the 250 kg wagon to make it go up with constant velocity:

a) If there is no friction.

b) If 𝜇 = 0.1.

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.drivers.system import System

mu = Symbol('mu')
alpha = math.radians(25)
m = 250
g = 9.81
W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
N = (0.0, m*g*math.sin(alpha))
Fr = (-mu*m*g*math.cos(alpha), 0.0)

body = Body('body', dimensions=2)

body.set('m', m)
body.apply_force('W', W)
body.apply_force('Fr', Fr)
body.apply_force('N', N)

universe = Universe()
universe.add_body(body)

a_x, a_y = universe.newton_equation('body').solve(['a_x', 'a_y'])
f_00 = m*a_x.subs('mu', 0.0)
f_01 = m*a_x.subs('mu', 0.1)
```

Solution:

```
f_00 = -1036.47 N
f_01 = -1258.74 N
```

#### <a name="sec-example-d2"></a>Example D-2

Statement: In the system shown in the figure, the three masses are mA = 1 kg, mB = 2 kg, and mC = 1.5 kg. If the coefficient of friction is 𝜇 = 0.223, calculate the acceleration of the system when it is released.

`# TODO include figure`

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.drivers.system import System

g = 9.81
mu = 0.223
alpha = math.radians(30)
ma, mb, mc = 1, 2, 1.5

Fra = (-mu*ma*g*math.cos(alpha), 0.0)
Frb = (-mu*mb*g, 0.0)
Wa = (-ma*g*math.sin(alpha), -ma*g*math.cos(alpha))
Wc = (mc*g, 0.0)

Tab = (Symbol('T2'), 0.0)
Tba = (-Symbol('T2'), 0.0)
Tbc = (Symbol('T1'), 0.0)
Tcb = (-Symbol('T1'), 0.0)

body_a = Body('A')
body_a.set('m', ma)
body_a.apply_force('T2', Tab)
body_a.apply_force('Fra', Fra)
body_a.apply_force('Wa', Wa)

body_b = Body('B')
body_b.set('m', mb)
body_b.apply_force('T1', Tbc)
body_b.apply_force('T2', Tba)
body_b.apply_force('Frb', Frb)

body_c = Body('C')
body_c.set('m', mc)
body_c.apply_force('Wc', Wc)
body_c.apply_force('T1', Tcb)

universe = Universe()
universe.add_body(body_a)
universe.add_body(body_b)
universe.add_body(body_c)

eq_a = universe.newton_equation('A')['x']
eq_b = universe.newton_equation('B')['x']
eq_c = universe.newton_equation('C')['x']

unkowns = ['T1', 'T2', 'a_x']

system = System()
system.add_equation(eq_a)
system.add_equation(eq_b)
system.add_equation(eq_c)

T1, T2, a_x = system.solve(unkowns)
```

Solution:

```
T1 = 13.54 N
T2 = 7.59 N
a_x = 0.79 m/s^2
```

#### <a name="sec-example-d3"></a>Example D-3

Statement: In the system shown in the figure, the three masses are mA = 1 kg, mB = 2 kg, and mC = 1.5 kg. If the coefficient of friction is 𝜇 = 0.223, calculate the acceleration of the system when it is released.

`# TODO include figure`

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.drivers.system import System

g = 9.81
mu = 0.223
alpha = math.radians(30)
ma = 1
mb = 2
mc = 1.5

Fra = (-mu*ma*g*math.cos(alpha), 0.0)
Frb = (-mu*mb*g, 0.0)
Wa = (-ma*g*math.sin(alpha), -ma*g*math.cos(alpha))
Wc = (mc*g, 0.0)

Tab = (Symbol('T2'), 0.0)
Tba = (-Symbol('T2'), 0.0)
Tbc = (Symbol('T1'), 0.0)
Tcb = (-Symbol('T1'), 0.0)

body = Body('body')
body.set('m', ma+mb+mc)
body.apply_force('T2', Tab)
body.apply_force('Fra', Fra)
body.apply_force('Wa', Wa)
body.apply_force('T1', Tbc)
body.apply_force('T2', Tba)
body.apply_force('Frb', Frb)
body.apply_force('Wc', Wc)
body.apply_force('T1', Tcb)

universe = Universe()
universe.add_body(body)

a_x, a_y = universe.newton_equation('body').solve(['a_x', 'a_y'])
```

Solution:

```
a = (0.79, -1.89) m/s^2
```

### <a name="sec-example-energy-conservation"></a>Energy conservation

#### <a name="sec-example-ec1"></a>Example EC-1

URL: https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/15._problemas_trabajo_y_energia_mecanica.pdf

Problem: 15.a

Statement: From the top of an inclined plane of 2 m in length and 30º of slope, a 500 g body is allowed to slide with an initial velocity of 1 m/s. Assuming that there is no friction during the journey, with what speed does it reach the base of the plane?

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe

m = 1.0
v0 = 1.0
alpha = math.radians(30)
length = 2.0
g = 9.81
h0 = length*math.sin(alpha)
hf = 0.0
vf = Symbol('vf')

Ep0 = m*g*h0
Ek0 = 1/2*m*v0**2
Epf = -m*g*hf
Ekf = -1/2*m*vf**2

body = Body('body', dimensions=2)

body.add_energy('Ep0', Ep0)
body.add_energy('Ek0', Ek0)
body.add_energy('Epf', Epf)
body.add_energy('Ekf', Ekf)

universe = Universe()
universe.add_body(body)

vf = universe.energy_conservation_equation('body').solve('vf')
```

Solution:

```
vf = 4.54 m/s
```

#### <a name="sec-example-ec2"></a>Example EC-2

URL: https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/15._problemas_trabajo_y_energia_mecanica.pdf

Problem: 15.a

Statement: From the top of an inclined plane of 2 m in length and 30º of slope, a 500 g body is allowed to slide with an initial velocity of 1 m/s. Assuming that there is no friction during the journey, plot the final velocity as a function of the initial velocity.

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe

file = 'vf_f_v0.png'

m = 1.0
v0 = Symbol('v0')
alpha = math.radians(30)
length = 2.0
g = 9.81
h0 = length*math.sin(alpha)
hf = 0.0
vf = Symbol('vf')

Ep0 = m*g*h0
Ek0 = 1/2*m*v0**2
Epf = -m*g*hf
Ekf = -1/2*m*vf**2

body = Body('body', dimensions=2)

body.add_energy('Ep0', Ep0)
body.add_energy('Ek0', Ek0)
body.add_energy('Epf', Epf)
body.add_energy('Ekf', Ekf)

universe = Universe()
universe.add_body(body)

universe.energy_conservation_equation('body').plot('vf', 'v0', [0, 4], points=200, path=file, show=False)
```

Solution:

![Plot of final velocity as a function of initial velocity](https://github.com/girdeux31/pyPhysics/blob/main/tests/ref/vf_f_v0.png?raw=true)

#### <a name="sec-example-ec3"></a>Example EC-3

URL: https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/15._problemas_trabajo_y_energia_mecanica.pdf

Problem: 15.b

Statement: If upon reaching the flat surface, it collides with a spring of constant k = 200 N/m, what distance will the spring compress?

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe

m = 0.5
k = 200.0
v0 = 1.0
alpha = math.radians(30)
length = 2.0
g = 9.81
h0 = length*math.sin(alpha)
hf = 0.0
vf = 0.0
dx = Symbol('dx')

Ep0 = m*g*h0
Ek0 = 1/2*m*v0**2
Epf = -m*g*hf
Ekf = -1/2*m*vf**2
Epe = -1/2*k*dx**2

body = Body('body', dimensions=2)

body.add_energy('Ep0', Ep0)
body.add_energy('Ek0', Ek0)
body.add_energy('Epf', Epf)
body.add_energy('Ekf', Ekf)
body.add_energy('Epe', Epe)

universe = Universe()
universe.add_body(body)

dx = universe.energy_conservation_equation('body').solve('dx')
```

Solution:

```
dx = 0.227 m
```

#### <a name="sec-example-ec4"></a>Example EC-4

URL: https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/15._problemas_trabajo_y_energia_mecanica.pdf

Problem: 20.c

Statement: A 3 kg block situated at a height of 4 m is allowed to slide down a smooth, frictionless curved ramp. When it reaches the ground, it travels 10 m on a rough horizontal surface until it stops. Calculate the coefficient of friction with the horizontal surface.

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe

m = 3.0
hc = 0.0
hb = 0.0
vc = 0.0
vb = 8.86
x = 10.0
g = 9.81
mu = Symbol('mu')

Epb = m*g*hb
Ekb = 1/2*m*vb**2
Epc = -m*g*hc
Ekc = -1/2*m*vc**2
Wfr = -mu*m*g*x

body = Body('body', dimensions=2)

body.add_energy('Epb', Epb)
body.add_energy('Ekb', Ekb)
body.add_energy('Epa', Epc)
body.add_energy('Eka', Ekc)
body.add_energy('Wfr', Wfr)

universe = Universe()
universe.add_body(body)

mu = universe.energy_conservation_equation('body').solve('mu', first_positive_root=True)
```

Solution:

```
mu = 0.40
```

### <a name="sec-example-gravity-field"></a>Gravitational field

#### <a name="sec-example-gf1"></a>Example GF-1

URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf

Problem: B1.a 2019 junio

Statement: A point mass A, MA = 3 kg, is located on the xy-plane, at the origin of coordinates. If a point mass B, MB = 5 kg, is placed at point (2, -2) m, determine the force exerted by mass A on mass B.

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.utils import magnitude

body_a = Body('A')
body_a.set('m', 3)
body_a.set('p', (0, 0))

body_b = Body('B')
body_b.set('m', 5)
body_b.set('p', (2, -2))

universe = Universe()
universe.add_body(body_a)
universe.add_body(body_b)

Fg_x, Fg_y = universe.gravitational_force_equation('B').solve(['Fg_x', 'Fg_y'])
Fg = magnitude((Fg_x, Fg_y))  # always positive value
```

Solution:

```
Fg = +1.25E-10 N
```

#### <a name="sec-example-gf2"></a>Example GF-2

URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf

Problem: B1.b 2019 junio

Statement: A point mass A, MA = 3 kg, is located on the xy-plane, at the origin of coordinates. If a point mass B, MB = 5 kg, is placed at point (2, -2) m, determine the work required to move mass B from point (2, -2) m to point (2, 0) m due to the gravitational field created by mass A.

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe

pa = (0, 0)
pb_0 = (2, -2)
pb_1 = (2, 0)

body_a = Body('A')
body_a.set('m', 3)
body_a.set('p', pa)

body_b = Body('B')
body_b.set('m', 5)

universe = Universe()
universe.add_body(body_a)
universe.add_body(body_b)

body_b.set('p', pb_0)

Ug_0 = universe.gravitational_potential_energy_equation('B').solve('Ug')

body_b.set('p', pb_1)

Ug_1 = universe.gravitational_potential_energy_equation('B').solve('Ug')

W = Ug_0[0] - Ug_1[0] # W = -AEp = Ug_0 - Ug_1
```

Solution:

```
W = 1.47E-10 J
```

#### <a name="sec-example-gf3"></a>Example GF-3

URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf

Problem: A1.a 2019 junio

Statement: A point mass m1 = 5 kg is located at the point (4, 3) m. Determine the intensity of the gravitational field created by mass m1 at the origin of coordinates.

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.utils import magnitude

body_a = Body('A')
body_a.set('m', 5)
body_a.set('p', (4, 3))
point = (0, 0)

universe = Universe()
universe.add_body(body_a)

g_x, g_y = universe.gravitational_field_intensity_equation(point).solve(['gg_x', 'gg_y'])
g = magnitude((g_x, g_y))  # always positive value
```

Solution:

```
g = +1.33E-11 m/s^2
```

### <a name="sec-example-electrical-field"></a>Electrical field

#### <a name="sec-example-ef1"></a>Example EF-1

URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F4.1-PAU-CampoEl%C3%A9ctrico.pdf

Problem: A3.a 2021 junio coincidentes

Statement: At the vertices of a square with a side of 2 m and centered at the origin of coordinates, four electric charges are placed as shown in the figure. Obtain the electric field created by the charges at the center of the square.

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe
from pyphysics.utils import magnitude

point = (0, 0)

body_1 = Body('1')
body_1.set('q', 5E-9)
body_1.set('p', (-1, +1))

body_2 = Body('2')
body_2.set('q', 5E-9)
body_2.set('p', (+1, +1))

body_3 = Body('3')
body_3.set('q', 3E-9)
body_3.set('p', (+1, -1))

body_4 = Body('4')
body_4.set('q', 3E-9)
body_4.set('p', (-1, -1))

universe = Universe()
universe.add_body(body_1)
universe.add_body(body_2)
universe.add_body(body_3)
universe.add_body(body_4)

Ee_x, Ee_y = universe.electrical_field_intensity_equation(point).solve(['Ee_x', 'Ee_y'])
Ee = magnitude((Ee_x, Ee_y))  # always positive value
```

Solution:

```
Ee = 12.72
```

#### <a name="sec-example-ef2"></a>Example EF-2

URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F4.1-PAU-CampoEl%C3%A9ctrico.pdf

Problem: A3.b 2021 junio coincidentes

Statement: At the vertices of a square with a side of 2 m and centered at the origin of coordinates, four electric charges are placed as shown in the figure. If an electron is launched from the center of the square with a velocity v = 3E4 j m/s, calculate the speed at which the electron will leave the square through the midpoint of the top side.

```
from pyphysics.drivers.body import Body, electron
from pyphysics.drivers.universe import Universe

point_0 = (0, 0)
point_1 = (0, 1)

body_1 = Body('1')
body_1.set('q', 5E-9)
body_1.set('p', (-1, +1))

body_2 = Body('2')
body_2.set('q', 5E-9)
body_2.set('p', (+1, +1))

body_3 = Body('3')
body_3.set('q', 3E-9)
body_3.set('p', (+1, -1))

body_4 = Body('4')
body_4.set('q', 3E-9)
body_4.set('p', (-1, -1))

universe = Universe()
universe.add_body(body_1)
universe.add_body(body_2)
universe.add_body(body_3)
universe.add_body(body_4)
universe.add_body(electron)

electron.set('p', point_0)

Ue_0 = universe.electrical_potential_energy_equation('electron').solve('Ue')

electron.set('p', point_1)

Ue_1 = universe.electrical_potential_energy_equation('electron').solve('Ue')

W = Ue_0[0] - Ue_1[0] # W = -AUe = Ue_0 - Ue_1
```

Solution:

```
W = 1.97E-18 J
```

#### <a name="sec-example-ef3"></a>Example EF-3

URL: https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F4.1-PAU-CampoEl%C3%A9ctrico.pdf

Problem: A3.b 2023 modelo

Statement: A hollow spherical shell with a radius of 3 cm and centered at the origin of coordinates is charged with a uniform surface charge density σ = 2 µC/m2. Obtain the work done by the electric field to move a particle with a charge of 1 nC from the point (0, 2, 0) m to the point (3, 0, 0) m.

```
from pyphysics.drivers.body import Body
from pyphysics.drivers.universe import Universe

point_0 = (0, 2, 0)
point_1 = (3, 0, 0)

sphere = Body('sphere', dimensions=3)
sphere.set('q', 22.62E-9)
sphere.set('p', (0, 0, 0))

point = Body('point', dimensions=3)
point.set('q', 1E-9)

universe = Universe(dimensions=3)
universe.add_body(sphere)
universe.add_body(point)

point.set('p', point_0)

Ue_0 = universe.electrical_potential_energy_equation('point').solve('Ue')

point.set('p', point_1)

Ue_1 = universe.electrical_potential_energy_equation('point').solve('Ue')

W = Ue_0[0] - Ue_1[0] # W = -AEp = Ue_0 - Ue_1
```

Solution:

```
W = 3.393E-8 J
```

## <a name="sec-bugs-limitations"></a>Bugs and limitations

`# TODO Limitation with p being the unknown`

## <a name="sec-licence"></a>License

This project includes MIT License. A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

## <a name="sec-contact"></a>Contact

Feel free to contact mesado31@gmail.com for any suggestion or bug.

> [!IMPORTANT]
> Visit GitHub page at https://github.com/girdeux31/pyPhysics
