# Bai 14:
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    
    s_lower = s.lower()
    
    for char in s_lower:
        if char in vowels:
            count += 1
            
    return count

chuoi_nhap = input("Nhập một chuỗi bất kỳ: ")
so_luong = count_vowels(chuoi_nhap)
print(f"Số lượng nguyên âm xuất hiện trong chuỗi là: {so_luong}")
