print("--- CHẠY BÀI 9 ---")
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Tiếng kêu động vật")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Gâu gâu")

cho = Dog("Cậu Vàng")
print(f"Tên chú chó: {cho.name}")
cho.sound()
print("-" * 30)
