class TVProgram:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for elem in self.items:
            if elem.uid == indx:
                self.items.remove(elem)
                break


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.name]
        except:
            return property()

    def __set__(self, instance, value):
        if self.name == '_uid' and isinstance(value, int) and value >= 1:
            instance.__dict__[self.name] = value
        elif self.name == '_duration' and isinstance(value, int):
            instance.__dict__[self.name] = value
        elif isinstance(value, str):
            instance.__dict__[self.name] = value


class Telecast:
    uid = Descriptor()
    name = Descriptor()
    duration = Descriptor()

    def __init__(self, uid, name, duration):
        self.uid = uid
        self.name = name
        self.duration = duration







