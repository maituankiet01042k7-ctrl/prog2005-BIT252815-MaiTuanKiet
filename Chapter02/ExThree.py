# Bai 3
try:
    n = int(input("Nhập số lượng số Fibonacci cần in (n): "))
    if n > 0:
        a, b = 0, 1
        count = 0
        print("Dãy Fibonacci:", end=" ")
        while count < n:
            print(a, end=" ")
            nth = a + b
            a = b
            b = nth
            count += 1
        print() 
    else:
        print("Vui lòng nhập n lớn hơn 0.")
except ValueError:
    print("Dữ liệu không hợp lệ.")
