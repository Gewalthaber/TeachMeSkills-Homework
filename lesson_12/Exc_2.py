from random import choice

class BeeElephant:

    def __init__(self, bee: int=50, elephant: int=50):
        self.bee = bee
        self.elephant = elephant

    def eat(self, meal: str, value: int):

        if meal == "nectar":
            self.bee += value
            self.elephant -= value
        elif meal == "grass":
            self.elephant += value
            self.bee -= value
        else:
            print("Неизвестная еда")
            return

        self.bee = max(0, self.bee)
        self.elephant = max(0, self.elephant)

    def status(self):
        return f"Пчела: {self.bee}, Слон: {self.elephant}"

    def random_feeding(self, value: int):
        meal = choice(["nectar", "grass"])
        print(f"Корм: {meal}")
        self.eat(meal, value)

        if self.bee >= 100:
            print(f"Пчела: {self.bee}, Слон: {self.elephant}")
            print("Пчела съела слона")
            exit()
        elif self.elephant >= 100:
            print(f"Пчела: {self.bee}, Слон: {self.elephant}")
            print("Слон съел пчелу")
            exit()

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant >= self.bee:
            print("tu-tu-do-do")
        else:
            print("wzzzz")

if __name__ == "__main__":
    creature = BeeElephant()
    print(creature.status())

    for i in range(20):
        creature.random_feeding(20)
        print(creature.status())
        creature.fly()
        creature.trumpet()




