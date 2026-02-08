# Bai 8
try:
    n = int(input("Nhập một số dương: "))
    if n > 0:
        reversed_n = str(n)[::-1]
        print(f"Số đảo ngược: {reversed_n}")
    else:
        print("Vui lòng nhập số dương.")
except ValueError:
    print("Dữ liệu không hợp lệ.")
