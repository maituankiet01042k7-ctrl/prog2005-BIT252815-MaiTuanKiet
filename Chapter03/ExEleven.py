# Bai 11:
input_string = input("Nhập các số (cách nhau bởi khoảng trắng): ")
arr = [float(x) for x in input_string.split()]

if len(arr) == 0:
    print("Danh sách trống!")
else:
    max_val = arr[0]
    min_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
            
    print(f"Giá trị lớn nhất: {max_val}")
    print(f"Giá trị nhỏ nhất: {min_val}")
