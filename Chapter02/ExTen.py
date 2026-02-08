# Bai 10
def tinh_tong(n):
    if n == 1:
        return 1
    else:
        return n + tinh_tong(n - 1)

try:
    num = int(input("Nhập n (để tính tổng từ 1 đến n): "))
    if num >= 1:
        print(f"Tổng các số từ 1 đến {num} là: {tinh_tong(num)}")
    else:
        print("Vui lòng nhập n >= 1.")
except ValueError:
    print("Dữ liệu không hợp lệ.")
