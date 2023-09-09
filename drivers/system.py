from sympy import solve, Symbol


class System:
    
    def __init__(self):

        self.equations = list()
        self.unknowns = list()

    def add_equation(self, equation):

        if not hasattr(equation, 'function'):
            raise TypeError(f'Cannot add object of type {type(equation).__name__}')

        self.equations.append(equation.function)

    def solve(self, unknowns):

        for unknown in unknowns:
            if not isinstance(unknown, str):
                raise TypeError(f'Unknown must be str not {type(unknown).__name__}')

        for equation in self.equations:

            eq_unknowns = [str(unknown) for unknown in equation.free_symbols]
            
            for eq_unknown in eq_unknowns:
                if eq_unknown not in unknowns:
                    raise RuntimeError(f'Unknwon {eq_unknown} not in system unkowns {unknowns}')

        unknowns = [Symbol(unknown) for unknown in unknowns]
        solution = solve(self.equations, unknowns, dict=True)

        if not solution:
            raise ValueError('System solution not found')

        if len(solution) != 1:
            raise ValueError('System has several solution')

        return solution[0].values()
