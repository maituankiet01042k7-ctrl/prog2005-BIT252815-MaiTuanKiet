# Bai 15
ten = input("Nhập tên sinh viên: ")
toan = float(input("Nhập điểm Toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))

dtb = (toan + ly + hoa) / 3

print(f"Sinh viên: {ten}")
print(f"Điểm trung bình: {dtb}")
