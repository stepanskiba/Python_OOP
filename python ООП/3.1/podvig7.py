class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        for elem in self.apps:
            if type(elem) == type(app):
                return
        self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = 'ВКонтакте'


class AppYouTube:
    def __init__(self, memory_max):
        self.name = 'YouTube'
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = 'Phone'
        self.phone_list = phone_list


pass