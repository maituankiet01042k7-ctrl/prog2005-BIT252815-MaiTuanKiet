# Bài 4
class Book:
    def __init__(self, name="", price=0):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

book1 = Book("Sách Toán", 120000)
print(f"Giá trị price của đối tượng: {book1.price}")
