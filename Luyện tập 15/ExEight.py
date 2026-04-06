class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Giá (price) không được nhỏ hơn 0")
        self._price = value

if __name__ == "__main__":
    sp1 = Product(100)
    print(f"Giá sản phẩm 1: {sp1.price}")
    
    try:
        sp2 = Product(-50)
    except ValueError as e:
        print(f"Báo lỗi khi tạo sản phẩm 2: {e}")
