# ==================== BÀI 3 ====================
print("\n--- Bài 3 ---")
while True:
    n = int(input("Nhập một số từ 1 đến 9: "))
    if 1 <= n <= 9:
        break
    print("Số không hợp lệ, vui lòng nhập lại!")

print(f"Bảng cửu chương của {n}:")
for i in range(1, 10):
    print(f"{n} x {i} = {n * i}")
