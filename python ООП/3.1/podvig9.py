class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        if not instance:  # этот костыль нужен, чтобы провурку на декоратор @property пройти.
            return property()
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key == 'MIN_DIMENSION' or key == 'MAX_DIMENSION':
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        elif type(value) in (int, float) and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            object.__setattr__(self, key, value)


d = Dimensions(1, 2, 3)
