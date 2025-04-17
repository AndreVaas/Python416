# Доступ через декоратор @Property
import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, n):
        self.__num = n

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, s):
        if not isinstance(s, str):
            raise TypeError("Фамилия должна быть строкой")
        f = s.split()
        letters = "".join(re.findall(r"[a-zа-яё-]", s, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
        for s in f:
            # print(s.strip(letters))
            if len(s.strip(letters)) != 0:
                raise TypeError("В фамилии можно использовать только буквы и дефис")
        self.__surname = s

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, p):
        if isinstance(p, int) or isinstance(p, float):
            self.__percent = p
        else:
            raise ValueError("Проценты должны быть целым или вещественным числом")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        if isinstance(v, int) or isinstance(v, float):
            self.__value = v
        else:
            raise ValueError("Баланс должен быть целым или вещественным числом")

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.__num} принадлежащий {self.surname} был закрыт.")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {round(usd_val, 2)} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {round(eur_val, 2)} {Account.suffix_eur}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс {round(self.value, 2)} {Account.suffix}")

    def print_info(self):
        print("Информация о счете: ")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent}%")
        print("-" * 20)


acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_balance()
# acc.percent = 1
# acc.num = "189281726"
# acc.surname = "Vasilev"
# acc.value = 10
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()

# acc.edit_owner("Дюма")
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()

# Доступ через get_...() и set_...()
# import re
#
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def set_num(self, num):
#         self.__num = num
#
#     def set_surname(self, s):
#         if not isinstance(s, str):
#             raise TypeError("Фамилия должна быть строкой")
#         f = s.split()
#         letters = "".join(re.findall(r"[a-zа-яё-]", s, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В фамилии можно использовать только буквы и дефис")
#         self.__surname = s
#
#     def set_percent(self, percent):
#         if isinstance(percent, int) or isinstance(percent, float):
#             self.__percent = percent
#         else:
#             raise ValueError("Проценты должны быть целым или вещественным числом")
#
#     def set_value(self, v):
#         if isinstance(v, int) or isinstance(v, float):
#             self.__value = v
#         else:
#             raise ValueError("Баланс должен быть целым или вещественным числом")
#
#     def get_num(self):
#         return self.__num
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {round(usd_val, 2)} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {round(eur_val, 2)} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {round(self.__value, 2)} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# # acc.print_balance()
# # acc.set_percent(5)
# acc.set_value(2232.2323)
#
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# # acc.edit_owner("12321323")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()
# acc.set_surname("Djonson")
