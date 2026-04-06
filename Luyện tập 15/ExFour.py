# BÀI 4
def bai_4():
    m1 = float(input("Nhập điểm môn 1: "))
    m2 = float(input("Nhập điểm môn 2: "))
    m3 = float(input("Nhập điểm môn 3: "))

    dtb = (m1 + m2 + m3) / 3
    print(f"Điểm trung bình: {dtb:.2f}")

    if dtb >= 8.0:
        print("Xếp loại: Giỏi")
    elif 6.5 <= dtb < 8.0:
        print("Xếp loại: Khá")
    elif 5.0 <= dtb < 6.5:
        print("Xếp loại: Trung bình")
    else:
        print("Xếp loại: Yếu")


if __name__ == "__main__":
    bai_4()
