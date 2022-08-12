class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for j in range(m)] for i in range(n)]

    def res(self, n, m):
        self.cells = [[Cell(1.0 + j + i * m) for j in range(m)] for i in range(n)]


table = TableSheet(5, 3)
table.cells[1][2] = Cell(3.4)
[[print(elem.value, end=' ') for elem in x] for x in table.cells]
table.res(5, 3)
[[print(elem.value, end=' ') for elem in x] for x in table.cells]
c = Cell(3.0)
print(c.value)
print(Cell.__dict__)
print(c.__dict__)