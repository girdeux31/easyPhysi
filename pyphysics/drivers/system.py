from sympy import solve, Symbol


class System:
    
    def __init__(self):

        self.equations = dict()
        self.unknowns = list()
        self.current_idx = 0

    def __getitem__(self, key):

        if not isinstance(key, str):
            raise ValueError('Parameter \'idx\' must be a string')
        
        if key not in self.equations.keys():
            raise ValueError(f'Key \'{key}\' not found in system with keys {self.equations.keys()}')

        return self.equations[key]

    def add_equation(self, equation, key=None):

        if not hasattr(equation, 'function'):
            raise TypeError(f'Cannot add object of type {type(equation).__name__}')

        self.unknowns += [str(unknown) for unknown in equation.function.free_symbols]

        if key:
            self.equations[key] = equation
        else:
            self.equations[self.current_idx] = equation
            self.current_idx += 1

    def solve(self, unknowns):

        if not self.equations:
            raise RuntimeError('Before solving system you must add equations with \'add_equation\' method')

        for unknown in unknowns:

            if not isinstance(unknown, str):
                raise TypeError(f'Unknown must be str not {type(unknown).__name__}')
            
            if unknown not in self.unknowns:
                raise RuntimeError(f'Unknwon \'{unknown}\' not in system unkowns {self.unknowns}')

        unknowns = [Symbol(unknown) for unknown in unknowns]
        functions = [equation.function for equation in self.equations.values()]  # TODO is the order kept?
        solution = solve(functions, unknowns, dict=True)

        if not solution:
            raise ValueError('System solution not found')

        if len(solution) != 1:
            raise ValueError('System has several solution')

        return solution[0].values()  # TODO return as dict?
