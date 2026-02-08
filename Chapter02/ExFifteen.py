# Bai 15
try:
    n = int(input("Nhập số nguyên dương: "))
    if n > 0:
        temp = n
        tong = 0
        while temp > 0:
            digit = temp % 10
            tong += digit
            temp //= 10
        print(f"Tổng các chữ số của {n} là: {tong}")
    else:
        print("Vui lòng nhập số nguyên dương.")
except ValueError:
    print("Dữ liệu không hợp lệ.")
