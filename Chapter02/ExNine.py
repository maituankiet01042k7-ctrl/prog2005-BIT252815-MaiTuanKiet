# Bai 9
try:
    n = int(input("Nhập số nguyên dương 5 chữ số: "))
    s_n = str(n)
    if n > 0 and len(s_n) == 5:
        max_digit = 0
        for char in s_n:
            digit = int(char)
            if digit > max_digit:
                max_digit = digit
        print(f"Chữ số lớn nhất trong {n} là: {max_digit}")
    else:
        print("Vui lòng nhập đúng số nguyên dương có 5 chữ số.")
except ValueError:
    print("Dữ liệu không hợp lệ.")
