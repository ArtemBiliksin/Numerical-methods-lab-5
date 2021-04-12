import numpy as np


class MethodBase:
    def __init__(self, n, f):
        self.__h = 1 / n
        self.__f = f
        self.dict_methods = self.__get_dict_methods()

    @property
    def h(self):
        return self.__h

    def method_euler(self, x, y):
        return y + self.h * self.__f(x, y)

    def method_cauchy(self, x, y):
        return y + self.h * self.__f(x + self.h / 2, y + (self.h / 2) * self.__f(x, y))

    def __get_dict_methods(self):
        return {'метод Эйлера': self.method_euler, 'метод Коши': self.method_cauchy}


class Method(MethodBase):
    def __init__(self, n):
        super().__init__(n, Method.__f)
        self.__get_methods()

    def method_trapezium(self, x, y):
        return (2 * y + self.h * self.__f(x, y)) / (2 - self.h * self.__f(x + self.h, 1))

    def __get_methods(self):
        self.dict_methods['метод трапеций'] = self.method_trapezium

    @staticmethod
    def __f(x, y):
        return 30 * y * (x - 0.2) * (x - 0.7)


class SolutionCauchyProblem:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.x_data = np.linspace(0, 1, arg)
        else:
            self.x_data = arg
        self.y_data = 0.1 * np.exp(self.x_data * (10 * (self.x_data * self.x_data) - 13.5 * self.x_data + 4.2))

    @staticmethod
    def name_tex_notation():
        return r'$y(x)=0.1 \cdot e^{10x^3-13.5x^2+4.2x}$'

    @staticmethod
    def name():
        return 'y(x)=0.1exp(10x^3-13.5x^2+4.2x)'
