import matplotlib.pyplot as plt

from sympy import Eq, solve


class Equation:

    def __init__(self, function, rhs=0.0):

        self.function = Eq(function, rhs)
        self.unknowns = [str(unknown) for unknown in self.function.free_symbols]

    def _get_first_positive_root(self, roots):

        for root in roots:

            if root.free_symbols:
                raise ValueError('Roots must be numeric not expressions, try setting argument \'first_positive_root=False\'')

            if not hasattr(root, '__float__'):
                raise ValueError('Roots must be convertible to float, try setting argument \'first_positive_root=False\'')
        
        positive_roots = [root for root in roots if root > 0.0]

        if len(positive_roots) == 0:
            raise RuntimeError('No positive roots are found, try setting argument \'first_positive_root=False\'')

        if len(positive_roots) > 1:
            raise RuntimeError('Several positive roots are found, try setting argument \'first_positive_root=False\'')

        return positive_roots[0]

    def solve(self, unknown, first_positive_root=False):
        
        if unknown not in self.unknowns:
            raise ValueError(f'Unknown \'{unknown}\' not in equation unkowns {self.unknowns}')

        roots = solve(self.function, unknown)

        if first_positive_root:
            root = self._get_first_positive_root(roots)

        return root if first_positive_root else roots

    def plot(self, independent, dependent, x_range, points=100, path=None, show=True):

        # Checks
        
        if len(self.unknowns) != 2:
            raise RuntimeError(f'Equation must have exactly two unknowns, but it has ({self.unknowns})')

        if independent not in self.unknowns:
            raise RuntimeError(f'Independent unknown ({independent}) is not in equation unknowns ({self.unknowns})')

        if dependent not in self.unknowns:
            raise RuntimeError(f'Dependent unknown ({dependent}) is not in equation unknowns ({self.unknowns})')

        if len(x_range) != 2:
            raise ValueError('Parameter \'x_range\' must have length 2')

        # Solve for independent unknown

        function = self.solve(independent)

        if not function or len(function) != 1:
            raise RuntimeError(f'Equation solution not found or several solutions found for {independent} unkown')

        # Get x,y points and plot

        dx = (x_range[1]-x_range[0]) / points
        x_list = [x_range[0]+dx*i for i in range(points)]
        y_list = [function[0].subs(dependent, x) for x in x_list]

        plt.plot(x_list, y_list)

        plt.title(f'{independent} = ' + str(function[0]))
        plt.xlabel(dependent)
        plt.ylabel(f'{independent}')
        plt.grid()

        if path:
            plt.savefig(path)

        if show:
            plt.show()