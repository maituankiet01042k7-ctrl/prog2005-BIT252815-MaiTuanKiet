# Bai 9:
input_string = input("Nhập các số nguyên (cách nhau bởi khoảng trắng): ")
arr = [int(x) for x in input_string.split()]

print("Các số lẻ trong danh sách là:")
for num in arr:
    if num % 2 != 0:
        print(num, end=" ")
