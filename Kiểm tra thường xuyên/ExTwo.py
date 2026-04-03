# Bài 2
danh_sach_ten = []
for i in range(5):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    danh_sach_ten.append(ten)
print("Danh sách sau khi nhập:", danh_sach_ten)

if len(danh_sach_ten) >= 2:
    del danh_sach_ten[1]
print("Danh sách sau khi xóa vị trí thứ hai:", danh_sach_ten)
