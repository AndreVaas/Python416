from logging.config import stopListening


class Automobile:

    def __init__(self, model, year, manufacturer, engine_power, color, price):
        self.__model = model
        self.__manufacturer = manufacturer
        self.__engine_power = engine_power
        self.__color = color

        if isinstance(year, int):
            self.__year = year
        else:
            print("Год выпуска должен быть целым числом.")
            self.__year = "Неизвестно"

        if isinstance(price, int) and price >= 0:
            self.__price = price
        else:
            print("Цена должна быть положительным числом.")
            self.__price = "Неизвестно"

    def set_model(self, model):
        self.__model = model

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_engine_power(self, engine_power):
        self.__engine_power = engine_power

    def set_color(self, color):
        self.__color = color

    def set_year(self, year):
        self.__year = year

    def set_price(self, price):
        self.__price = price

    def get_model(self):
        return self.__model

    def get_year(self, year):
        return self.__year

    def get_manufacturer(self):
        return self.__manufacturer

    def get_engine_power(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Модель: {self.__model}\n"
              f"Год выпуска: {self.__year}\n"
              f"Производитель:{self.__manufacturer}\n"
              f"Мощность двигателя:{self.__engine_power}\n"
              f"Цвет автомобиля:{self.__color}\n"
              f"Стоимость: {self.__price}")
        print("=" * 40)


auto1 = Automobile("X7 M50i", 2021, "BMW", "530 л.с.", "white",
                   10790000)
auto1.print_info()

