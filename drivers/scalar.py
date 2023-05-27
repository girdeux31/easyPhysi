
from sympy import Symbol


class Scalar:

    def __init__(self, name, value=None):

        self.name = name

        self.value = value if value else self._get_default_value()

    def __str__(self):

        return self.name

    def _get_default_value(self):

        return Symbol(self.name)

    def undefine(self):

        self.value = self._get_default_value()
    
    def define(self, value):

        self.value = value 
