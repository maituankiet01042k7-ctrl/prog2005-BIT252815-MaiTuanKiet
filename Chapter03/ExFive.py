# Bai 5:
input_string = input("Nhập các số thực (cách nhau bởi khoảng trắng): ")
arr = [float(x) for x in input_string.split()]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key > arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Danh sách sau khi sắp xếp giảm dần (Insertion Sort):", arr)
