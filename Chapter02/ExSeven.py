# Bai 7
try:
    a = int(input("Nhập số nguyên dương thứ nhất: "))
    b = int(input("Nhập số nguyên dương thứ hai: "))

    if a > 0 and b > 0:
        x, y = a, b
        while y != 0:
            x, y = y, x % y
        print(f"Ước số chung lớn nhất của {a} và {b} là: {x}")
    else:
        print("Vui lòng nhập hai số nguyên dương.")
except ValueError:
    print("Dữ liệu không hợp lệ.")
