print("--- CHẠY BÀI 6 ---")
class Product:
    def __init__(self, price):
        self.price = price  

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Giá trị truyền vào phải > 0")

    def __str__(self):
        return f"Thông tin price của product: {self._price}"

sp = Product(25000)
print(sp)
print("-" * 30)
