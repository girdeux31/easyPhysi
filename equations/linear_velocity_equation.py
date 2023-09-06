
from ..drivers.axes import Axes
from ..drivers.equation import Equation


class LinearVelocityEquation:
    
    def __init__(self, universe):

        self.universe = universe
        self.axes = Axes(self.universe.dimensions)
    
    def _equation(self, body, axis):

        # equation to solve is v0-v + g*t = 0
        
        foo = body.initial_velocity.value[axis] - body.velocity.value[axis] \
                    + body.gravity.value[axis]*body.time.value

        return Equation(foo)

    def solve(self, body, unknown, axis=None, first_positive_root=False):
        # TODO first positive root does not make sense with velocity

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
