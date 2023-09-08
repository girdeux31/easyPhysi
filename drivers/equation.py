from sympy import Eq
from sympy import solve


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

    def solve(self, unknown, first_positive_root):

        if unknown not in self.unknowns:
            raise ValueError(f'Unknown \'{unknown}\' not found')

        roots = solve(self.function, unknown)

        if first_positive_root:
            root = self._get_first_positive_root(roots)

        return root if first_positive_root else roots
