# BÀI 1
def bai_1():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    print(f"Tổng: {a + b}")
    print(f"Hiệu: {a - b}")
    print(f"Tích: {a * b}")
    if b != 0:
        print(f"Thương: {a / b}")
    else:
        print("Thương: Không thể chia cho 0")

if __name__ == "__main__":
    bai_1()
