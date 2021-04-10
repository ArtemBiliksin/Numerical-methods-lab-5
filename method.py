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
        method_names = ['метод Эйлера', 'метод Коши']
        methods = [self.method_euler, self.method_cauchy]
        return dict(zip(method_names, methods))


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

