# Bai 12
try:
    n = int(input("Nhập n: "))
    tong_le = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            tong_le += i
    print(f"Tổng các số lẻ từ 1 đến {n} là: {tong_le}")
except ValueError:
    print("Dữ liệu không hợp lệ.")
