
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class NewtonEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)

    def _equation(self, body, axis):

        foo = 0.0

        # equation to solve is \sum F - m*a = 0
        
        for force in body.forces:
            foo += force.value[axis]

        foo -= body.mass.value*body.acceleration.value[axis]
        
        return Equation(foo)

    def solve(self, body, unknown, axis=None, first_positive_root=False):

        if axis:

            if axis not in self.axes.components.keys():
                raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')

            root = self._solve_one_axis(body, unknown, axis, first_positive_root)

        else:

            root = self._solve_all_axes(body, unknown, first_positive_root)

        return root

    def _solve_one_axis(self, body, unknown, axis, first_positive_root):

        axis = self.axes.components[axis]
        equation = self._equation(body, axis)
        root = equation.solve(unknown, first_positive_root)

        return root

    def _solve_all_axes(self, body, unknown, first_positive_root):

        roots = list()

        for axis in self.axes.components.keys():

            root = self._solve_one_axis(body, unknown, axis, first_positive_root)
            roots.append(root)

        return tuple(roots)

