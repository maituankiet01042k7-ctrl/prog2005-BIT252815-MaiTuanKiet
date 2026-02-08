# Bai 5
s = input("Nhập chuỗi: ")
char = input("Nhập ký tự cần đếm: ")

if len(char) == 1:
    count = s.count(char)
    print(f"Ký tự '{char}' xuất hiện {count} lần trong chuỗi.")
else:
    print("Vui lòng chỉ nhập một ký tự.")
