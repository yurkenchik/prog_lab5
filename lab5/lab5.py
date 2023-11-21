# Клас, який представляє взуття (кросівки)
class Sneakers:
    def __init__(self, brand, size, color, price, quantity, material, numberOfSales):

        # Конструктор для ініціалізації об'єкта Sneakers
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.material = material
        self.numberOfSales = numberOfSales

    def __str__(self):

        # Строкове представлення об'єкта Sneakers для зручного виведення
        return f"{self.brand} - Size: {self.size}, Color: {self.color}, Price: {self.price}, Quantity: {self.quantity}, Material: {self.material}, Sales: {self.numberOfSales}"


# Клас, який представляє магазин спортивного взуття
class SportShoesStore:
        def __init__(self):
            # Конструктор для ініціалізації об'єкта SportShoesStore з порожнім інвентарем
            self.inventory = []

        def add_sneakers(self, sneakers):
            # Метод для додавання кросівок до інвентарю магазину
            self.inventory.append(sneakers)

        def sort_by_price(self):
            # Метод для сортування інвентарю за ціною в порядку зростання
            self.inventory = sorted(self.inventory, key=lambda x: x.price)

        def sort_by_quantity(self):
            # Метод для сортування інвентарю за кількістю в порядку спадання
            self.inventory = sorted(self.inventory, key = lambda x: x.quantity, reverse = True)

        def top_sallers(self, top_n = 5):
            # Метод для вибору топ продавців на основі кількості продажів
            self.inventory  = sorted(self.inventory, key = lambda x: x.numberOfSales, reverse = True)[:top_n]


# Кількість пробілів для відділення виведених рядків
number_of_spaces = 100
    

# Створення екземпляра магазину
store = SportShoesStore()


# Створення об'єктів класу Sneakers
sneaker1 = Sneakers("Nike", 10, "Black", 150, 50, "Leather", 100)
sneaker2 = Sneakers("Adidas", 9, "White", 120, 30, "Mesh", 80)
sneaker3 = Sneakers("Asics", 11, "Black", 100, 20, "Synthetic", 120)
sneaker4 = Sneakers("New Balance", 11, "Green", 100, 20, "Synthetic", 120)
sneaker5 = Sneakers("Fila", 11, "Red", 100, 20, "Synthetic", 190)
sneaker6 = Sneakers("Converse", 11, "White", 100, 20, "Synthetic", 120)
sneaker7 = Sneakers("Puma", 11, "White", 100, 20, "Synthetic", 150)
sneaker8 = Sneakers("Vans", 11, "White", 100, 20, "Synthetic", 150)
sneaker9 = Sneakers("Fred Perry", 11, "White", 100, 20, "Synthetic", 160)
sneaker10 = Sneakers("vans", 11, "White", 100, 20, "Synthetic", 120)


# Додавання кросівок до інвентарю магазину
store.add_sneakers(sneaker1)
store.add_sneakers(sneaker2)
store.add_sneakers(sneaker3)
store.add_sneakers(sneaker4)
store.add_sneakers(sneaker5)
store.add_sneakers(sneaker6)
store.add_sneakers(sneaker7)
store.add_sneakers(sneaker8)
store.add_sneakers(sneaker9)
store.add_sneakers(sneaker10)


# Виведення інвентарю до сортування за ціною
print("*" * number_of_spaces)
print("IINVENTORY BEFORE SORTING: ")
print("*" * number_of_spaces)
for sneaker in store.inventory:
    print(sneaker)


# Сортування інвентарю за ціною
store.sort_by_price()
print("*" * number_of_spaces)
print("INVENTORY AFTER SORTING BY PRICE: ")
print("*" * number_of_spaces)
for sneaker in store.inventory:
    print(sneaker)


# Сортування інвентарю за кількістю
store.sort_by_quantity()
print("*" * number_of_spaces)
print("INVENTORY AFTER SORTING BY QUANTITY: ")
print("*" * number_of_spaces)
for sneaker in store.inventory:
    print(sneaker)


# Вибір топ продавців
store.top_sallers()
print("*" * number_of_spaces)
print("TOP SELLERS: ")
print("*" * number_of_spaces)
for sneaker in store.inventory:
    print(sneaker)
# Виклик екземпляра як функції
store()

# Виведення інформації про магазин
print(store)

