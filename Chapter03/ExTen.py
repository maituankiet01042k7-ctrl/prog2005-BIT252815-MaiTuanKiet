# Bai 10:
input_string = input("Nhập các số nguyên (cách nhau bởi khoảng trắng): ")
arr = [int(x) for x in input_string.split()]

tong_chan = 0
print("Các số chẵn trong danh sách là:")

for num in arr:
    if num % 2 == 0:
        print(num, end=" ")
        tong_chan += num

print(f"\nTổng của các số chẵn đó là: {tong_chan}")
