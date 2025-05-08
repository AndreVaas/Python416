from Car.Car import Car


class Electrocar(Car):
    def __init__(self, brand, model, year, mileage, charge):
        super().__init__(brand, model, year, mileage)
        self.charge = charge

    def __call__(self, *args, **kwargs):
        print(f"{self.brand},{self.model},{self.year},{self.mileage}\n"
              f"Этот автомобиль имеет мощность: {self.charge}%")


