# Bai 6
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)

try:
    num = int(input("Nhập số cần tính giai thừa: "))
    if num >= 0:
        print(f"Giai thừa của {num} là: {giai_thua(num)}")
    else:
        print("Không tồn tại giai thừa cho số âm.")
except ValueError:
    print("Dữ liệu không hợp lệ.")
