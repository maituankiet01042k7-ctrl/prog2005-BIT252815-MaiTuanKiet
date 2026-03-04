# Bai 7:
input_string = input("Nhập các số (cách nhau bởi khoảng trắng): ")
arr = [float(x) for x in input_string.split()]
target = float(input("Nhập số cần tìm: "))

vi_tri = -1 # Giả sử ban đầu chưa tìm thấy

for i in range(len(arr)):
    if arr[i] == target:
        vi_tri = i
        break # Tìm thấy thì thoát vòng lặp ngay

if vi_tri != -1:
    print(f"Tìm thấy số {target} tại chỉ số (index) thứ {vi_tri}.")
else:
    print(f"Không tìm thấy số {target} trong danh sách.")
