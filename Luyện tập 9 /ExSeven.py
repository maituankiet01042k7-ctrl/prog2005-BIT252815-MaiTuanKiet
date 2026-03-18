print("--- CHẠY BÀI 7 ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string_data):
        name, age = string_data.split('-')
        return cls(name, int(age))

p = Person.from_string("Nam-20")
print(f"Đối tượng tạo từ chuỗi -> Tên: {p.name}, Tuổi: {p.age}")
print("-" * 30)
