
from sympy import Eq
from sympy import solve


class Equation:

    def __init__(self, function, rhs=0.0):

        self.function = Eq(function, rhs)
        self.unknowns = [str(unknown) for unknown in self.function.free_symbols]

    def solve(self, unknown):

        if unknown not in self.unknowns:
            raise ValueError(f'Unknown \'{unknown}\' not found')

        return solve(self.function, unknown)