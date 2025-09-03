class Bus:
    def __init__(self, speed: int, max_seats: int, max_speed: float, passenger: str=None):
        self.speed = speed
        self.max_seats = max_seats
        self.free_seat = True
        self.max_speed = max_speed
        self.passengers = []
        self.seats = {i: None for i in range(1, max_seats + 1)}

        if passenger:
            self.passengers.append(passenger)
            self._occupy_first_free_seat(passenger)

        self.free_seat = len(self.get_free_seats()) > 0

    def _occupy_first_free_seat(self, passenger: str):
        for seat_number, occupant in self.seats.items():
            if occupant is None:
                self.seats[seat_number] = passenger
                self.free_seat = len(self.get_free_seats()) > 0
                return True
        return False

    def get_free_seats(self):
        return [seat for seat, occupant in self.seats.items() if occupant is None]

    def get_occupied_seats(self):
        return [seat for seat, occupant in self.seats.items() if occupant is not None]

    def __iadd__(self, passenger: str):
        if len(self.passengers) < self.max_seats:
            self.passengers.append(passenger)
            self.free_seat = len(self.passengers) < self.max_seats
            return self
        else:
            print("Нет свободных мест")
            return self

    def __isub__(self, passenger: str):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            self.free_seat = len(self.passengers) < self.max_seats
            return self
        return self

    def __str__(self):
        return f"Автобус: скорость: {self.speed} км/ч, количество мест: {self.max_seats}, количество пассажиров: {len(self.passengers)}"

    def add_speed(self, speed):
        new_speed = self.speed + speed
        if new_speed > self.max_speed:
            print("Указанная скорость не может превышать максимальной!")
            print(f"Ваша скорость {self.max_speed} км/ч")
        else:
            self.speed = new_speed
            print(f"Ваша скорость {self.speed} км/ч")

    def remove_speed(self, speed):
        new_speed = self.speed - speed
        if new_speed < 0:
            print("Скорость автобуса не может быть отрицательной!")
            print("Ваша скорость 0 км/ч. Автобус остановлен!")
        else:
            self.speed = new_speed
            print(f"Ваша скорость {self.speed} км/ч")

bus_1 = Bus(60, 3, 120, None)
print(bus_1)
bus_1 += "Иванов"
print(bus_1)
bus_1 += "Пивасов"
bus_1.add_speed(int(input("На сколько повысить скорость?: ")))
bus_1.remove_speed(int(input("На сколько снизить скорость?: ")))
print(bus_1)










