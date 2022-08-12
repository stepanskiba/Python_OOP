class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    lst_msg = []

    @staticmethod
    def add_message(msg):
        Viber.lst_msg.append(msg)

    @staticmethod
    def remove_message(msg):
        Viber.lst_msg.remove(msg)

    @staticmethod
    def set_like(msg):
        msg.fl_like = not(msg.fl_like)

    @staticmethod
    def show_last_message(num):
        print(*Viber.lst_msg[num::-1])

    @staticmethod
    def total_messages():
        return len(Viber.lst_msg)