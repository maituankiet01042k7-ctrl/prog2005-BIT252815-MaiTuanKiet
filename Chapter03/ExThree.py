# Bai 3:
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
print("Danh sách màu ban đầu:", colors)

try:
    colors.remove("Green")
    print("Đã xóa màu 'Green' thành công.")
except ValueError:
    print("Lỗi: Màu 'Green' không có trong danh sách.")

print("Danh sách màu sau thao tác:", colors)
