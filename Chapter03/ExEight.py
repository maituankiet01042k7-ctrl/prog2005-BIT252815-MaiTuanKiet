# Bai 8:
input_string = input("Nhập các số (cách nhau bởi khoảng trắng): ")
arr = [float(x) for x in input_string.split()]

tim_thay = False

for num in arr:
    if num > 10:
        print(f"Số đầu tiên lớn hơn 10 trong danh sách là: {num}")
        tim_thay = True
        break

if not tim_thay:
    print("Không có số nào lớn hơn 10 trong danh sách.")
