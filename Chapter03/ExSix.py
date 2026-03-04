# Bai 6:
input_string = input("Nhập các số nguyên (cách nhau bởi khoảng trắng): ")
arr = [int(x) for x in input_string.split()]

n = len(arr)
so_lan_hoan_doi = 0

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # Hoán đổi 2 phần tử
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            so_lan_hoan_doi += 1

print("Danh sách sau khi sắp xếp tăng dần (Bubble Sort):", arr)
print(f"Tổng số lần hoán đổi đã thực hiện: {so_lan_hoan_doi}")
