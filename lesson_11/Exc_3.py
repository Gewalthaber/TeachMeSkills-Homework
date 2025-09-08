class Car:
    def __init__(self, name, color, type, year):
        self.name = name
        self.color = color
        self.type = type
        self.year = year

    def __str__(self):
        return f"Автомобиль: {self.name} [цвет: {self.color}, тип: {self.type}, год выпуска: {self.year}]"

    def starting_engine(self):
        return "Двигатель автомобиля заведен"

    def stop_engine(self):
        return "Двигатель автомобиля заглушен"

car_1 = Car("Volkswagen", "черный", "Внедорожник", 2020)
engine_1 = car_1.starting_engine()
print(car_1)
print(engine_1)
