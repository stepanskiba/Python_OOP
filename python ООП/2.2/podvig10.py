class PhoneBook:
    def __init__(self):
        #self.lst_of_num = []
        self.lst_of_obj = []

    def add_phone(self, phone):
        #self.lst_of_num.append(phone.number)
        self.lst_of_obj.append(phone)

    def remove_phone(self, indx):
        #self.lst_of_num.pop(indx)
        self.lst_of_obj.pop(indx)

    def get_phone_list(self):
        return self.lst_of_obj


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)