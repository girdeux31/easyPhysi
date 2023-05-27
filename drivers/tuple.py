
from sympy import Symbol
from .axes import Axes


class Tuple:

    def __init__(self, name, dimensions=2, value=None):

        if dimensions != 2 and dimensions != 3:
            raise ValueError('Parameter \'dimensions\' must be 2 or 3')

        self.name = name
        self.dimensions = dimensions

        self.axes = Axes(self.dimensions)
        self.value = value if value else self._get_default_value()

    def __str__(self):

        return f'{self.name}_{self.dimensions}n'

    # def __index__(self):  # TODO define

    #     pass

    def _get_default_value(self):

        output = tuple()
        
        for _ in self.axes.components:
            output += (Symbol(self.name),)

        return output

    def undefine(self, axis=None):

        if axis:
            
            if axis not in self.axes.components.keys():
                raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')
            
            self.value = self.value[:axis] + (Symbol(self.name),) + self.value[axis+1:]

        else:

            self.value = tuple()
        
            for _ in self.axes.components.keys():
                self.value += (Symbol(self.name),)
    
    def define(self, value, axis=None):

        if axis:
            
            if axis not in self.axes.components.keys():
                raise ValueError(f'Parameter \'axis\' must be one of these {self.axes.components.keys()}')
            
            axis = self.axes.components[axis]
            self.value = self.value[:axis] + (value,) + self.value[axis+1:]

        else:

            if len(value) != self.dimensions:
                raise ValueError(f'Parameter \'value\' must be of length {self.dimensions}')

            self.value = value
        

