# BÀI 9
def bai_9():
    chuoi = input("Nhập một chuỗi ký tự: ")
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(chuoi)
    print("Đã lưu chuỗi vào file output.txt")

if __name__ == "__main__":
    bai_9()
