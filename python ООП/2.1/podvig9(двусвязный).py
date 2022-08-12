class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        lst = []
        x = self.head
        while x:
            lst.append(x.get_data())
            x = x.get_next()
        return lst


class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


#ob = ObjList('данные 1')
#lst = LinkedList()
#lst.add_obj(ObjList("данные 1"))
#lst.add_obj(ObjList("данные 2"))
#lst.add_obj(ObjList("данные 3"))
#print(lst.head.get, lst.tail)
#res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
a = b = 3
print(a, b)
a = 4
#b = 5
print(a, b)