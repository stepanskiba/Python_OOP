class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and type(value) is str:
            object.__setattr__(self, key, value)
        elif (key == 'practices' or key == 'duration') and type(value) is int and value >= 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item != 'title' and item != 'practices' and item != 'duration':
            object.__delattr__(self, item)

    def __getattr__(self, item):
        return False


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, lesson):
        self.modules.append(lesson)

    def remove_module(self, indx):
        self.modules.pop(indx)






