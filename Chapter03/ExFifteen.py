 Bai 15:
text = input("Nhập chuỗi cần đảo ngược: ")

reversed_slicing = text[::-1]
print(f"Cách 1 (Sử dụng Slicing): {reversed_slicing}")

reversed_loop = ""
for char in text:
    reversed_loop = char + reversed_loop
    
print(f"Cách 2 (Không dùng Slicing): {reversed_loop}")
