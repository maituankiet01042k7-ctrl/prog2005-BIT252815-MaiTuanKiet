# Bai 13:
text = input("Nhập chuỗi cần kiểm tra: ")

clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("Đây LÀ chuỗi đối xứng (Palindrome).")
else:
    print("Đây KHÔNG PHẢI là chuỗi đối xứng.")
