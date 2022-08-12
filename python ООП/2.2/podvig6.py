class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @staticmethod
    def check_obj(obj):
        return isinstance(obj, StackObj) or obj is None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if self.check_obj(obj):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        x = self.top
        if x is None:
            return
        while x and x.next != self.last:
            x = x.next
        if x:
            x.next = None
        last = self.last
        self.last = x
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        x = self.top
        lst = []
        while x:
            lst.append(x.data)
            x = x.next
        return lst


st = Stack()
st.push(StackObj('data 1'))
st.push(StackObj('data 2'))
st.push(StackObj('data 3'))
st.pop()
print(st.get_data())