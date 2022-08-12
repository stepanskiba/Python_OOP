class Money:
    def __init__(self, money):
        self.__money = money

    @staticmethod
    def __check_money(money):
        return type(money) == int and money >= 0

    def get_money(self):
        return self.__money

    def set_money(self, money):
        if Money.__check_money(money):
            self.__money = money

    def add_money(self, mn):
        self.__money += mn.__money