import re
from random import randint
from string import ascii_lowercase, ascii_uppercase, digits

s = ascii_lowercase + ascii_uppercase + digits + '_.'


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if email.count('..') > 0:
            return False
        if re.fullmatch(r'[A-Za-z0-9_.]{1,101}@[A-Za-z0-9_.]{1,51}', email):
            if email.count('.', email.index('@')) == 1:
                return True
        return False

    @classmethod
    def get_random_email(cls):
        l = randint(1, 101)
        ans = ''
        for _ in range(l):
            ans += s[randint(1, len(s) - 1)]
        return ans + '@gmail.com'






assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email("sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email("sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email("sc.lib@listru") == False and EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"