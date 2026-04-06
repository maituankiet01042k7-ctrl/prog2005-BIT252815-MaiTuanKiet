# BÀI 5
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    chuoi_dau_vao = input("Nhập chuỗi cần đếm nguyên âm: ")
    so_luong = count_vowels(chuoi_dau_vao)
    print(f"Số lượng nguyên âm: {so_luong}")
