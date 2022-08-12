import time

class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot = [0, 0, 0]

    def add_filter(self, slot_num, filter):
        if self.slot[slot_num - 1] == 0:
            #print(type(filter) == Calcium, slot_num)
            if slot_num == 1 and type(filter) == Mechanical:
                #print(2)
                self.slot[0] = filter
            if slot_num == 2 and type(filter) == Aragon:
                self.slot[1] = filter
            if slot_num == 3 and type(filter) == Calcium:
                #print(3)
                self.slot[2] = filter

    def remove_filter(self, slot_num):
        self.slot[slot_num - 1] = 0

    def get_filters(self):
        return tuple(self.slot)

    def water_on(self):
        if self.slot[0] != 0 and self.slot[1] != 0 and self.slot[2] != 0:
            #print('a')
            if all(map(lambda x: 0 <= time.time() - x.date < self.MAX_DATE_FILTER , self.slot)):
                return True
            return False
        return False


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(w)
#print(my_water.slot)
my_water.add_filter(3, Calcium(time.time()))
print(my_water.water_on())
#print(my_water.get_filters())

