# <a name="sec-top"></a>easyPhysi

> [!WARNING]
> **Library under development yet**

easyPhysi is a physics library to solve pre-universitary physics problems. The physics areas that are covered by pyPhisics are summarized hereafter. See the [main structure](#sec-main-structure) to use easyPhysi and also some [examples](#sec-examples).

 - Kinematics
 - Dynamics
 - Energy conservation
 - Gravitational field
 - Electrical field

The main characteristics for easyPhysi are summarized in the following table.

<a name="tab-characteristics"></a>

 | Characteristic   | Value         |
 |------------------|---------------|
 | Name             | easyPhysi     |
 | Version          | 1.0.0         |
 | Author           | Carles Mesado |
 | Date             | 22/12/2023    |
 | Size             | ~ 18 KiB      |

## <a name="sec-index"></a>0. Index

0. [Index](#sec-index)
1. [Installation](#sec-installation)
2. [Usage](#sec-usage)
    - [Main structure](#sec-main-structure)
    - [Properties](#sec-properties)
    - [Special bodies](#sec-special-bodies)
    - [Equations](#sec-equations)
    - [Advance features](#sec-advance-features)
3. [Examples](#sec-examples)
    - [Kinematics](#sec-example-kinematics)
    - [Dynamics](#sec-example-dynamics)
    - [Energy conservation](#sec-example-energy-conservation)
    - [Gravitational field](#sec-example-gravitational-field)
    - [Electrical field](#sec-example-electrical-field)
4. [Bugs and limitations](#sec-bugs-limitations)
5. [Changelog](#secchange-log)
6. [License](#sec-licence)
7. [Contact](#sec-contact)

## <a name="sec-installation"></a>1. Installation

> [!WARNING]
> **Package not in pypi yet**

> [!NOTE]
> easyPhysi is developed and tested with Python 3.10.

Install the package with pip,

`pip install easyPhysi`

or clone the GitHub repository.

`gh repo clone girdeux31/easyPhysi`

The following third-party modules are requirements.

 - matplotlib>=3.7.0
 - scipy>=1.11.0
 - sympy==1.12

## <a name="sec-usage"></a>2. Usage

### <a name="sec-main-structure"></a>2.0. Main structure

Most pre-university physics problems can be solved following this structure composed of a few lines.

```
from easyPhysi.drivers.universe import Universe
from easyPhysi.drivers.body import Body

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

> [!NOTE]
> See [Example](#sec-example-ef2) for a 3D problem.

### <a name="sec-properties"></a>2.1. Properties

The following properties can be defined in any body.

> [!NOTE]
> Property names are case sensitive.

<a name="tab-properties"></a>

 |Property |Description                     |Type      |Components           |
 |---------|--------------------------------|----------|---------------------|
 |a        |Acceleration                    |Vector    |(a_x, a_y[, a_z])    |
 |q        |Charge                          |Scalar    |q                    |
 |Ee       |Electrical field intensity      |Vector    |(Ee_x, Ee_y[, Ee_z]) |
 |Fe       |Electrical force                |Vector    |(Fe_x, Fe_y[, Fe_z]) |
 |Ue       |Electrical potential energy     |Scalar    |Ue                   |
 |Ve       |Electrical potential            |Scalar    |Ve                   |
 |gg       |Gravitational field intensity   |Vector    |(gg_x, gg_y[, gg_z]) |
 |Fg       |Gravitational force             |Vector    |(Fg_x, Fg_y[, Fg_z]) |
 |Ug       |Gravitational potential energy  |Scalar    |Ug                   |
 |Vg       |Gravitational potential         |Scalar    |Vg                   |
 |g        |Gravity                         |Vector    |(g_x, g_y[, g_z])    |
 |p0       |Initial position                |Vector    |(p0_x, p0_y[, p0_z]) |
 |v0       |Initial velocity                |Vector    |(v0_x, v0_y[, v0_z]) |
 |m        |Mass                            |Scalar    |m                    |
 |p        |Position                        |Vector    |(p_x, p_y[, p_z])    |
 |t        |Time                            |Scalar    |t                    |
 |v        |Velocity                        |Vector    |(v_x, v_y[, v_z])    |
 
Use `set` method in an instanciated body to define its property and define its value according to its type. See value types in [Section](#sec-property-types).

> [!NOTE]
> Units are up to the user. Eventhough SI is recommended, other systems can be used provided that different units are consistent.

> [!NOTE]
> Force and energy cannot be defined as properties since each force and energy is defined by its own formula, see [Section](#sec-property-nondefined).

#### <a name="sec-property-types"></a>2.1.0. Property types

There are two types of properties: **scalars** (for example `m` for mass) and **vectors** (for example `g` for gravity).

##### <a name="sec-property-type-scalar"></a>2.1.0.i Scalars

They are integers of floats, examples follow.

```
body.set('prop', 250)       # int
body.set('prop', 5.0E-9)    # float
```

##### <a name="sec-property-type-vectors"></a>2.1.0.ii Vectors

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

#### <a name="sec-property-nondefined"></a>2.1.1. Non-defined properties

Force (mainly used in `newton_equation`) and energy (mainly used in `energy_conservation_equation`) cannot be defined as properties in an instanciated body with `set` method (note that they are not listed in [Table](#tab-equations)). Instead they can be defined in an instanciated body with `apply_force` and `add_energy` methods respectively.

```
body.apply_force('my_force', value)
body.add_energy('my_energy', value)
```

This is designed on purpose because many different forces and energies can be applied/added to a body and they have different algebraic expressions. Thus, the algebraic expression for the force and energy must be defined by the user.

See examples for Newton equation and energy conservation equation in [Dynamic Examples](#sec-example-dynamics) and [Energy Conservation Examples](#sec-example-energy-conservation) respectively.

### <a name="sec-special-bodies"></a>2.2. Special bodies

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

Import them using the following line and use them without instanciating the body or defining its main properties, see [Example](#sec-example-ef1).

`from easyPhysi.drivers.body import special_body`
 
### <a name="sec-equations"></a>2.3. Equations

The following equations can be solved. Each equation is a method defined in the `Universe` class.

> [!NOTE]
> Equation names are case sensitive.

<a name="tab-equations"></a>  # TODO E and F should be removed

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
 
Use any of these equation in an instance of universe and include the body the equation applies to. Then use the `solve` method and include the unknown(s) to be solved, see third column in  table above.

`universe.physics_equation('my_body').solve('my_unknown')`

#### <a name="sec-equation-types"></a>2.3.0. Equation types

There are two types of equations: scalar (for example `energy_conservation_equation`) and vectorial (for example `newton_equation`).

##### <a name="sec-equation-type-scalar"></a>2.3.0.i Scalar

Only one unknown is accepted.

```
out = universe.physics_equation('my_body').solve('my_unk')
```

##### <a name="sec-equation-type-vectorial"></a>2.3.0.ii Vectorial

As many unknowns as universe dimensions are accepted, these must be defined as a list and passed as argument of `solve` method. Vector components must be append to unknown names, such as `a_x` and `a_y` for acceleration, see [Section](#sec-property-type-vectors) and forth column in [Table](#tab-properties). The same number of unknowns must be defined as outputs, no name restriction apply for output unknowns.

```
out_x, out_y = universe.physics_equation('my_body').solve(['unk_x', 'unk_y'])
```

### <a name="sec-advance-features"></a>2.4. Advance features

The most useful features are already defined. However, for the sake of completeness, a few more features for the advance user are defined in this section.

#### <a name="sec-other-feature-magnitude"></a>2.4.0. Vector module

Vectorial equations give results as vector components. A function is available to obtain its module or _magnitude_, see [Example](#sec-example-k0).

```
from easyPhysi.utils import magnitude
prop = magnitude((prop_x, prop_y))
```

#### <a name="sec-other-feature-functions"></a>2.4.1. Working with functions

Equations return numerical values if there is only one unknown (all properties are defined but one), but return functions if there is more than one unknown (two or more properties are left undefined). Use \'subs\' method to replace an unknown by a specified numerical value, see [Example](#sec-example-d0).

```
foo = universe.physics_equation('body').solve('my_unk')
out = foo.subs('my_sym', value)
```

#### <a name="sec-other-feature-systems"></a>2.4.2. Solving system of equations

System of equations can be defined -with `System` class- and solved with `solve` method. The `solve` method accepts a list with as many unknowns as equations defined in the system, see [Example](#sec-example-d2).

```
equation = universe.physics_equation('body').solve('my_unk')
system = System()
system.add_equation(equation)

# define and add as meny equations as needed

x, y, z = system.solve(['x', 'y', 'z'])
```

#### <a name="sec-other-feature-plot"></a>2.4.3. Plotting equations

Method `plot` can be used over any equation to plot unknowns in the form of function `independent = f(dependent)`.

`universe.physics_equation('my_body').plot(independent, dependent, x_range, points=100, path=None, show=True)`

Arguments are described hereafter.

 - `independent`: if equation is [scalar](#sec-equation-type-scalar), then only one independent unknown is expected. If equation is [vectorial](#sec-equation-type-vectorial), then exactly the same number of universe dimensions are expected as independent unknowns (as a list). See examples below.
 - `dependent`: exactle one unknown is expected.
 - `x_range`: range to plot for dependent unknown (x-axis).
 - `points`: number of points to plot, optional argument, default is 100.
 - `path`: path to save image as file, optional argument, by default it is None and no image is saved.
 - `show`: if `True` the plot is shown on screen, optional argument, by default it is `True`.

See a plot for scalar equation in [Example](#sec-example-ec1).

#### <a name="sec-other-feature-equation"></a>2.4.4. Get equation from system

In some cases, it is only interesting to solve a specific equation from a vectorial equation (that is a set of equations or a system). The method 'get_equation' can be used over any vectorial equation to return the specific equation, the axis component is expected as argument to the method, see [Example](#sec-example-k0).

`universe.pyshics_equation('my_body').get_equation('axis')`

## <a name="sec-examples"></a>3. Examples

### <a name="sec-example-kinematics"></a>3.0. Kinematics

#### <a name="sec-example-k0"></a>3.0.0. Example K-0

[Problem 10](https://fq.iespm.es/documentos/janavarro/fisica2bach/T0_vectores_cinematica.pdf)

A ball falls from a roof located 10 m high, forming a 30º angle with the horizontal, with a speed of 2 m/s. Calculate:

a) At what distance from the wall does it hit the ground?

b) The speed it has when it reaches the ground (disregard air friction).

```
import math

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.utils import magnitude

alpha = math.radians(-30)
g = (0.0, -9.81)
p0 = (0.0, 10.0)
v0 = (2.0*math.cos(alpha), 2.0*math.sin(alpha))
py = 0.0

body = Body('body')  # by default 2D

body.set('g', g)
body.set('p0', p0)
body.set('v0', v0)
body.set('p_y', py)

universe = Universe()  # by default 2D
universe.add_body(body)

t = universe.linear_position_equation('body').get_equation('y').solve('t')

body.set('t', t[1])

p_x = universe.linear_position_equation('body').get_equation('x').solve('p_x')

v_x, v_y = universe.linear_velocity_equation('body').solve(['v_x', 'v_y'])
v = magnitude((v_x, v_y))
```

> [!TIP]
> Solution: `p_x[0] = 2.30 m, v = 14.15 m/s`

### <a name="sec-example-dynamics"></a>3.1. Dynamics

#### <a name="sec-example-d0"></a>3.1.0. Example D-0

[Problem 14](https://fq.iespm.es/documentos/rafael_artacho/4_ESO/08.%20Problemas%20Las%20fuerzas.pdf)

The following ramp has an inclination of 25º. Determine the force that must be exerted on the 250 kg wagon to make it go up with constant velocity:

a) If there is no friction.

b) If 𝜇 = 0.1.

```
import math
from sympy import Symbol

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.drivers.system import System

mu = Symbol('mu')
alpha = math.radians(25)
m = 250
g = 9.81
W = (-m*g*math.sin(alpha), -m*g*math.cos(alpha))
N = (0.0, m*g*math.sin(alpha))
Fr = (-mu*m*g*math.cos(alpha), 0.0)

body = Body('body')

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

> [!TIP]
> Solution: `f_00 = -1036.47 N, f_01 = -1258.74 N`

#### <a name="sec-example-d1"></a>3.1.1. Example D-1

Following previous example, calculate the angle if the acceleration is known.

```
import math
from sympy import Symbol

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.drivers.system import System

mu = 0.1
sin_alpha = Symbol('sin_alpha')
cos_alpha = Symbol('cos_alpha')
m = 250
g = 9.81
a = (-5.03497308675920, -4.74499424315328)  # from previous example
W = (-m*g*sin_alpha, -m*g*cos_alpha)
N = (0.0, m*g*sin_alpha)
Fr = (-mu*m*g*cos_alpha, 0.0)

body = Body('body')

body.set('m', m)
body.set('a', a)
body.apply_force('W', W)
body.apply_force('Fr', Fr)
body.apply_force('N', N)

universe = Universe()
universe.add_body(body)

sin_alpha, cos_alpha = universe.newton_equation('body').solve(['sin_alpha', 'cos_alpha'])

alpha_from_sin = 90.0 - math.degrees(math.asin(sin_alpha))
alpha_from_cos = 90.0 - math.degrees(math.acos(cos_alpha))
```

> [!TIP]
> Solution: `alpha_from_sin = 25º, alpha_from_cos = 25º`

#### <a name="sec-example-d2"></a>3.1.2. Example D-2

In the system shown in the figure, the three masses are mA = 1 kg, mB = 2 kg, and mC = 1.5 kg. If the coefficient of friction is 𝜇 = 0.223, calculate the acceleration of the system when it is released.

![System of three masses](https://github.com/girdeux31/easyPhysi/blob/main/tests/ref/system_dynamics.png?raw=true)

```
import math
from sympy import Symbol

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.drivers.system import System

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

> [!TIP]
> Solution: `T1 = 13.54 N, T2 = 7.59 N, a_x = 0.79 m/s2`

#### <a name="sec-example-d3"></a>3.1.3. Example D-3

In the system shown in the figure, the three masses are mA = 1 kg, mB = 2 kg, and mC = 1.5 kg. If the coefficient of friction is 𝜇 = 0.223, calculate the acceleration of the system when it is released.

![System of three masses](https://github.com/girdeux31/easyPhysi/blob/main/tests/ref/system_dynamics.png?raw=true)

```
import math
from sympy import Symbol

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.drivers.system import System

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

> [!TIP]
> Solution: `a = (0.79, -1.89) m/s2`

### <a name="sec-example-energy-conservation"></a>3.2. Energy conservation

#### <a name="sec-example-ec0"></a>3.2.0. Example EC-0

[Problem 15.a](https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/15._problemas_trabajo_y_energia_mecanica.pdf)

From the top of an inclined plane of 2 m in length and 30º of slope, a 500 g body is allowed to slide with an initial velocity of 1 m/s. Assuming that there is no friction during the journey, with what speed does it reach the base of the plane?

```
import math
from sympy import Symbol

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe

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

body = Body('body')

body.add_energy('Ep0', Ep0)
body.add_energy('Ek0', Ek0)
body.add_energy('Epf', Epf)
body.add_energy('Ekf', Ekf)

universe = Universe()
universe.add_body(body)

vf = universe.energy_conservation_equation('body').solve('vf')
```

> [!TIP]
> Solution: `vf = 4.54 m/s`

#### <a name="sec-example-ec1"></a>3.2.1. Example EC-1

[Problem: 15.a](https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/15._problemas_trabajo_y_energia_mecanica.pdf)

From the top of an inclined plane of 2 m in length and 30º of slope, a 500 g body is allowed to slide with an initial velocity of 1 m/s. Assuming that there is no friction during the journey, plot the final velocity as a function of the initial velocity.

```
import math
from sympy import Symbol

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe

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

body = Body('body')

body.add_energy('Ep0', Ep0)
body.add_energy('Ek0', Ek0)
body.add_energy('Epf', Epf)
body.add_energy('Ekf', Ekf)

universe = Universe()
universe.add_body(body)

universe.energy_conservation_equation('body').plot('vf', 'v0', [0, 4], points=200, path=file, show=False)
```

![Plot of final velocity as a function of initial velocity](https://github.com/girdeux31/easyPhysi/blob/main/tests/ref/vf_f_v0.png?raw=true)

#### <a name="sec-example-ec2"></a>3.2.2. Example EC-2

[Problem 15.b](https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/15._problemas_trabajo_y_energia_mecanica.pdf)

If upon reaching the flat surface, it collides with a spring of constant k = 200 N/m, what distance will the spring compress?

```
import math
from sympy import Symbol

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe

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

body = Body('body')

body.add_energy('Ep0', Ep0)
body.add_energy('Ek0', Ek0)
body.add_energy('Epf', Epf)
body.add_energy('Ekf', Ekf)
body.add_energy('Epe', Epe)

universe = Universe()
universe.add_body(body)

dx = universe.energy_conservation_equation('body').solve('dx')
```

> [!TIP]
> Solution: `dx = 0.227 m`

#### <a name="sec-example-ec3"></a>3.2.3. Example EC-3

[Problem 20.c](https://fq.iespm.es/documentos/rafael_artacho/1_bachillerato/15._problemas_trabajo_y_energia_mecanica.pdf)

A 3 kg block situated at a height of 4 m is allowed to slide down a smooth, frictionless curved ramp. When it reaches the ground, it travels 10 m on a rough horizontal surface until it stops. Calculate the coefficient of friction with the horizontal surface.

```
from sympy import Symbol

from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe

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

body = Body('body')

body.add_energy('Epb', Epb)
body.add_energy('Ekb', Ekb)
body.add_energy('Epa', Epc)
body.add_energy('Eka', Ekc)
body.add_energy('Wfr', Wfr)

universe = Universe()
universe.add_body(body)

mu = universe.energy_conservation_equation('body').solve('mu')
```

> [!TIP]
> Solution: `mu[0] = 0.40`

### <a name="sec-example-gravity-field"></a>3.3. Gravitational field

#### <a name="sec-example-gf0"></a>3.3.0. Example GF-0

[Problem B1.a 2019 junio](https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf)

A point mass A, MA = 3 kg, is located on the xy-plane, at the origin of coordinates. If a point mass B, MB = 5 kg, is placed at point (2, -2) m, determine the force exerted by mass A on mass B.

```
from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.utils import magnitude

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

> [!TIP]
> Solution: `Fg = +1.25E-10 N`

#### <a name="sec-example-gf1"></a>3.3.1. Example GF-1

[Problem B1.b 2019 junio](https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf)

A point mass A, MA = 3 kg, is located on the xy-plane, at the origin of coordinates. If a point mass B, MB = 5 kg, is placed at point (2, -2) m, determine the work required to move mass B from point (2, -2) m to point (2, 0) m due to the gravitational field created by mass A.

```
from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe

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

> [!TIP]
> Solution: `W = 1.47E-10 J`

#### <a name="sec-example-gf2"></a>3.3.2. Example GF-2

[Problem A1.a 2019 junio](https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F2-PAU-Gravitacion.pdf)

A point mass m1 = 5 kg is located at the point (4, 3) m. Determine the intensity of the gravitational field created by mass m1 at the origin of coordinates.

```
from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.utils import magnitude

body_a = Body('A')
body_a.set('m', 5)
body_a.set('p', (4, 3))
point = (0, 0)

universe = Universe()
universe.add_body(body_a)

g_x, g_y = universe.gravitational_field_intensity_equation(point).solve(['gg_x', 'gg_y'])
g = magnitude((g_x, g_y))  # always positive value
```

> [!TIP]
> Solution: `g = +1.33E-11 m/s2`

### <a name="sec-example-electrical-field"></a>3.4. Electrical field

#### <a name="sec-example-ef0"></a>3.4.0. Example EF-0

[Problem A3.a 2021 junio coincidentes](https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F4.1-PAU-CampoEl%C3%A9ctrico.pdf)

At the vertices of a square with a side of 2 m and centered at the origin of coordinates, four electric charges are placed as shown in the figure. Obtain the electric field created by the charges at the center of the square.

```
from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe
from easyPhysi.utils import magnitude

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

> [!TIP]
> Solution: `Ee = 12.72 N/C`

#### <a name="sec-example-ef1"></a>3.4.1. Example EF-1

[Problem A3.b 2021 junio coincidentes](https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F4.1-PAU-CampoEl%C3%A9ctrico.pdf)

At the vertices of a square with a side of 2 m and centered at the origin of coordinates, four electric charges are placed as shown in the figure. If an electron is launched from the center of the square with a velocity v = 3E4 j m/s, calculate the speed at which the electron will leave the square through the midpoint of the top side.

```
from easyPhysi.drivers.body import Body, electron
from easyPhysi.drivers.universe import Universe

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

W = Ue_0[0] - Ue_1[0]  # W = -AUe = Ue_0 - Ue_1
```

> [!TIP]
> Solution: `W = 1.97E-18 J`

#### <a name="sec-example-ef2"></a>3.4.2. Example EF-2

[Problem A3.b 2023 modelo](https://gitlab.com/fiquipedia/drive.fiquipedia/-/raw/main/content/home/recursos/recursospau/ficherospaufisicaporbloques/F4.1-PAU-CampoEl%C3%A9ctrico.pdf)

A hollow spherical shell with a radius of 3 cm and centered at the origin of coordinates is charged with a uniform surface charge density σ = 2 µC/m2. Obtain the work done by the electric field to move a particle with a charge of 1 nC from the point (0, 2, 0) m to the point (3, 0, 0) m.

```
from easyPhysi.drivers.body import Body
from easyPhysi.drivers.universe import Universe

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

W = Ue_0[0] - Ue_1[0]  # W = -AEp = Ue_0 - Ue_1
```

> [!TIP]
> Solution: `W = 3.393E-8 J`

## <a name="sec-bugs-limitations"></a>4. Bugs and limitations

* Trigonometric functions are not able to handle symbols or expressions (for example `math.sin`, `math.cos` or `math.atan2`) and this error is shown: `TypeError: Cannot convert expression to float`. Therefore, position unknown (`p`) cannot be solved for the following equations:
    - electrical_field_intensity_equation
    - electrical_force_equation
    - gravitational_field_intensity_equation
    - gravitational_force_equation
* For the same reason, when defining forces for `newton_equation` with `apply_force` method, the angle cannot be set as un unkown as it is usually inside `math.sin` or `math.cos` functions. Fortunatelly, since the force algebraic formula is defined by the user, `sin_alpha` and `cos_alpha` can be set as unknowns instead of `math.sin(alpha)` or `math.cos(alpha)`. Then, easily get the angle with `math.asin`, `math.acos`, see [Example](#sec-example-d1).

## <a name="sec-changelog"></a>5. Changelog

* 25/06/23 - Initial idea
* 22/12/23 - v1.0.0 first stable version

## <a name="sec-licence"></a>6. License

This project includes MIT License. A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

## <a name="sec-contact"></a>7. Contact

Feel free to contact mesado31@gmail.com for any suggestion or bug.

> [!IMPORTANT]
> Visit GitHub page at https://github.com/girdeux31/easyPhysi
