class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __repr__(self):
        if self.taste is not None:
            return f"У Вас газировка со вкусом: {self.taste}"
        else:
            return "У Вас обычная газировка"

soda_1 = Soda("клубника")
print(soda_1)

soda_2 = Soda()
print(soda_2)
