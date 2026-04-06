# BÀI 3
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

def bai_3():
    n = int(input("Nhập số nguyên để tính giai thừa: "))
    print(f"Giai thừa của {n} là: {giai_thua(n)}")

if __name__ == "__main__":
    bai_3()
