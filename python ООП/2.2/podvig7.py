class RadiusVector2D:
    MIN_COORD, MAX_COORD = -100, 1024

    def __init__(self, x=0, y=0):
        if self.check(x):
            self.__x = x
        else:
            self.__x = 0
        if self.check(y):
            self.__y = y
        else:
            self.__y = 0

    @staticmethod
    def check(x):
        return type(x) in (int, float) and RadiusVector2D.MIN_COORD <= x <= RadiusVector2D.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.check(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.check(value):
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2


v3 = RadiusVector2D(10000, 200)
print(RadiusVector2D.check(-200))
print(v3.x)