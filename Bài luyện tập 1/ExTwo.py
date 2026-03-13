#==================== BÀI 2 ====================
print("\n--- Bài 2 ---")
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))

print(f"Lũy thừa ({so1}^{so2}): {so1**so2}")
print(f"Căn bậc 2 của {so1}: {math.sqrt(so1) if so1 >= 0 else 'Không hợp lệ (số âm)'}")
print(f"Căn bậc 2 của {so2}: {math.sqrt(so2) if so2 >= 0 else 'Không hợp lệ (số âm)'}")

if so2 != 0:
    print(f"Chia lấy phần nguyên: {so1 // so2}")
    print(f"Chia lấy phần dư: {so1 % so2}")
else:
    print("Không thể chia lấy phần nguyên/dư vì số thứ hai bằng 0")

print(f"Làm tròn số thứ nhất: {round(so1)}")
print(f"Làm tròn số thứ hai: {round(so2)}")
