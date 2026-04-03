# Bài 3
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

mang = list(map(int, input("Nhập mảng các số tự nhiên (cách nhau bởi dấu cách): ").split()))

so_le = [x for x in mang if x % 2 != 0]
print(f"Dòng 1: Các số lẻ {so_le} và tổng số lượng số lẻ: {len(so_le)}")

so_nguyen_to = [x for x in mang if is_prime(x)]
print(f"Dòng 2: Các số nguyên tố {so_nguyen_to}")
