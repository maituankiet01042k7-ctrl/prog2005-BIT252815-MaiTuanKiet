# Bai 4
try:
    n = int(input("Nhập một số: "))
    s = str(abs(n))
    tong = 0
    for char in s:
        tong += int(char)
    print(f"Tổng các chữ số của {n} là: {tong}")
except ValueError:
    print("Dữ liệu không hợp lệ.")
