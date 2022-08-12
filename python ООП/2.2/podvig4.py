class Car:
    @staticmethod
    def check(model):
        return type(model) == str and 2 <= len(model) <= 100

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if Car.check(model):
            self.__model = model

c = Car()
c.model = 'bmw'
print(c.model)