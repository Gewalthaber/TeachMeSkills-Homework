class Math:
    def addition(self, x, y):
        self.x = x
        self.y = y
        result_addition = self.x + self.y
        return f"Результат сложения: {result_addition}"

    def subtraction(self, x, y):
        self.x = x
        self.y = y
        result_subtraction = self.x - self.y
        return f"Результат вычитания: {result_subtraction}"

    def multiplication(self, x, y):
        self.x = x
        self.y = y
        result_multiplication = self.x * self.y
        return f"Результат умножения: {result_multiplication}"

    def division(self, x, y):
        self.x = x
        self.y = y
        result_division = self.x / self.y
        return f"Результат деления: {result_division}"

math = Math()

result_1 = math.addition(2, 3)
print(result_1)

result_2 = math.subtraction(4, 4)
print(result_2)

result_3 = math.multiplication(5, 5)
print(result_3)

result_4 = math.division(6, 6)
print(result_4)
