import re
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', number):
            return True
        return False

    @staticmethod
    def check_name(name):
        if re.fullmatch(r'[A-Z]{1,} [A-Z]{1,}', name):
            return True
        return False


print(CardCheck.CHARS_FOR_NAME)