
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class NewtonEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def __call__(self, name, axis=None):

        return self.equation(name, axis=axis)

    def _equation(self, body, axis):

        foo = 0.0

        # equation to solve is \sum F - m*a = 0
        
        for force in body.forces:
            foo += force[axis]

        foo -= body.mass()*body.acceleration[axis]
        
        return Equation(foo)

    def equation(self, name, axis=None):

        body = self.universe.get_body(name)

        if axis:

            if axis not in self.axes.components.keys():
                raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

            equation = self._equation_for_one_axis(body, axis)

        else:

            equation = self._equations_for_all_axes(body)

        return equation

    def _equation_for_one_axis(self, body, axis):

        axis = self.axes.components[axis]
        equation = self._equation(body, axis)

        return equation

    def _equations_for_all_axes(self, body):

        equations = list()

        for axis in self.axes.components.keys():

            equation = self._equation_for_one_axis(body, axis)
            equations.append(equation)

        return tuple(equations)
