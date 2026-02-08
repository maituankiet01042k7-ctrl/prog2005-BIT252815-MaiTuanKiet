# Bai 2
try:
    n = int(input("Nhập một số dương: "))
    if n > 0:
        tong_uoc = 0
        for i in range(1, n):
            if n % i == 0:
                tong_uoc += i
        
        if tong_uoc == n:
            print(f"{n} là số hoàn hảo.")
        else:
            print(f"{n} không phải là số hoàn hảo.")
    else:
        print("Vui lòng nhập số dương.")
except ValueError:
    print("Dữ liệu không hợp lệ.")
