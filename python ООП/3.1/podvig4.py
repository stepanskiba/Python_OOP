num = 1

class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    def __init__(self, name, weight, price):
        global num
        self.id = num
        num += 1
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name' and type(value) is str:
            object.__setattr__(self, key, value)
        elif (key == 'weight' or key == 'price' or key == 'id') and type(value) in (int, float) and value >= 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)






