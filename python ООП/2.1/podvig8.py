class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def get_coords(self):
        return (self.__sp, self.__ep)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.get_coords()[0].get_coords()} {self.get_coords()[1].get_coords()}")


rect = Rectangle(0, 0, 20, 34)




