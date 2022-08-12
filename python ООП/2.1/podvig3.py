class Clock:
    def __init__(self, time=0):
        self.__time = time

    @staticmethod
    def __check_time(tm):
        return type(tm) == int and 0 <= tm < 100_000

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock()
clock.set_time(12)
print(clock.get_time())
