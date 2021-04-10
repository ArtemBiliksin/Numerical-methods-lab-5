class MethodBase:

    def __init__(self, n, f):
        self.__h = 1 / n
        self.__f = f

    @property
    def h(self):
        return self.__h

    def method_euler(self, x, y):
        return y + self.h * self.__f(x, y)

    def method_cauchy(self, x, y):
        return y + self.h * self.__f(x + self.h / 2, y + (self.h / 2) * self.__f(x, y))


class Method(MethodBase):

    def __init__(self, n):
        super().__init__(n, Method.__f)

    def method_trapezium(self, x, y):
        return (2 * y + self.h * self.__f(x, y)) / (2 - self.h * self.__f(x + self.h, 1))

    @staticmethod
    def __f(x, y):
        return 30 * y * (x - 0.2) * (x - 0.7)
