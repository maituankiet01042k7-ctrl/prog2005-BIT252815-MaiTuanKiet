# Bai 11
try:
    dtb = float(input("Nhập điểm trung bình: "))
    if 0 <= dtb <= 10:
        if dtb >= 8.0:
            print("Xếp loại: Giỏi")
        elif dtb >= 6.5:
            print("Xếp loại: Khá")
        elif dtb >= 5.0:
            print("Xếp loại: Trung bình")
        else:
            print("Xếp loại: Yếu")
    else:
        print("Điểm không hợp lệ (phải từ 0 đến 10).")
except ValueError:
    print("Dữ liệu nhập vào không phải là số.")
