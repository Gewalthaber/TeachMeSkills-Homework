class Product:

    def __init__(self, product: str, shop: str, cost: float):
        self.__product = product
        self.__shop = shop
        self.__cost = cost

        if cost < 0:
            raise ValueError("Цена не может быть отрицательной")

    @property
    def product(self):
        return self.__product

    @property
    def shop(self):
        return self.__shop

    @property
    def cost(self):
        return self.__cost

    def __str__(self):
        return f"Товар: {self.__product}, Магазин: {self.__shop}, Цена: {self.__cost} руб."

    def __repr__(self):
        return f"Товар ({self.__product}, {self.__shop}, {self.__cost})"

    def __add__(self,other):
        if isinstance(other, Product):
            return self.__cost + other.__cost
        elif isinstance(other, (int, float)):
            return self.__cost + other
        else:
            raise ValueError("Можно складывать только с товаром или ценой")

class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        self.__products.append(product)

    def print_product_index(self, index: int):
        if index < 0 or index >= len(self.__products):
            raise IndexError(f"Индекс {index} выходит за пределы массива (0-{len(self.__products) - 1})")

        print(self.__products[index])

    def print_product_name(self, name: str):
        found = False
        for product in self.__products:
            if product.product.lower() == name.lower():
                print(product)
                found = True

            if not found:
                print(f"Товар с именем {name} не найден")

    def sort_by_products(self):
        self.__products.sort(key=lambda x: x.product)

    def sort_by_shop(self):
        self.__products.sort(key=lambda x: x.shop)

    def sort_by_cost(self):
        self.__products.sort(key=lambda x: x.cost)

    def print_all_products(self):
        return self.__products.copy()

    def __str__(self):
        if not self.__products:
            return "На складе нет товаров"

        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

if __name__ == "__main__":
    warehouse = Warehouse()

    warehouse.add_product(Product("Ноутбук", "5 элемент", 50000))
    warehouse.add_product(Product("Телефон", "Электросила", 25000))
    warehouse.add_product(Product("Планшет", "На Связи", 30000))
    warehouse.add_product(Product("Мышь", "МТС", 1500))

    print("=== Все товары на складе ===")
    print(warehouse)

    print("\n=== Поиск по индексу ===")
    warehouse.print_product_index(0)
    warehouse.print_product_index(2)

    print("\n=== Поиск по имени ===")
    warehouse.print_product_name("Телефон")
    warehouse.print_product_name("Ноутбук")
    warehouse.print_product_name("Монитор")  # Несуществующий товар

    print("\n=== Сортировка по цене ===")
    warehouse.sort_by_cost()
    print(warehouse)

    print("\n=== Сортировка по названию товара ===")
    warehouse.sort_by_products()
    print(warehouse)

    print("\n=== Сортировка по магазину ===")
    warehouse.sort_by_shop()
    print(warehouse)

    print("\n=== Перегрузка оператора сложения ===")
    product1 = Product("Клавиатура", "5 элемент", 2000)
    product2 = Product("Наушники", "МТС", 3500)

    total_price = product1 + product2
    print(f"Сумма цен {product1.product} и {product2.product}: {total_price} руб.")


