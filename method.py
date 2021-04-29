import numpy as np


class Method:
    def __init__(self, n):
        self.__h = 1 / n
        self.__f = lambda x, y: 30 * y * (x - 0.2) * (x - 0.7)
        self.dict_methods = {'метод Эйлера': self.__method_euler,
                             'метод Коши': self.__method_cauchy,
                             'метод трапеций': self.__method_trapezium}
        self.dict = Method.get_name_methods()
        self.x_data = np.linspace(0, 1, n)
        self.y_data_dict = self.__calculate_y_data_dict()

    def __method_euler(self, x, y):
        return y + self.__h * self.__f(x, y)

    def __method_cauchy(self, x, y):
        return y + self.__h * self.__f(x + self.__h / 2, y + (self.__h / 2) * self.__f(x, y))

    def __method_trapezium(self, x, y):
        return (2 * y + self.__h * self.__f(x, y)) / (2 - self.__h * self.__f(x + self.__h, 1))

    def __method_runge(self, x, y):
        h = self.__h
        f = self.__f
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + h / 2 * k1)
        k3 = h * f(x + h / 2, y + h / 2 * k2)
        k4 = h * f(x + h, y + h * k3)
        return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    @staticmethod
    def get_name_methods():
        return ['метод Эйлера', 'метод Коши', 'метод трапеций']

    def __calculate_y_data_dict(self):
        y_data_dict = dict(zip(self.dict_methods.keys(), [[0.1] for _ in range(len(self.dict_methods))]))
        for x in self.x_data[1:]:
            for method_name in self.dict_methods:
                y = self.dict_methods[method_name](x, y_data_dict[method_name][-1])
                y_data_dict[method_name].append(y)
        return y_data_dict


class SolutionCauchyProblem:
    def __init__(self, n):
        self.x_data = np.linspace(0, 1, n)
        self.y_data = 0.1 * np.exp(self.x_data * (10 * (self.x_data * self.x_data) - 13.5 * self.x_data + 4.2))

    @staticmethod
    def name_tex_notation():
        return r'$y(x)=0.1 \cdot e^{10x^3-13.5x^2+4.2x}$'

    @staticmethod
    def name():
        return 'y(x)=0.1exp(10x^3-13.5x^2+4.2x)'
