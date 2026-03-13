# ==================== BÀI 6 ====================
print("\n--- Bài 6 ---")
chuoi = "5; 7; 8; -2; 8; 11; 13; 9; 10"
danh_sach = [int(x.strip()) for x in chuoi.split(";")]

print("In từng số trên một dòng riêng:")
for so in danh_sach:
    print(so)

so_chan = sum(1 for x in danh_sach if x % 2 == 0)
print("Số lượng số chẵn:", so_chan)

so_am = sum(1 for x in danh_sach if x < 0)
print("Số lượng số âm:", so_am)

def kiem_tra_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

so_nguyen_to = sum(1 for x in danh_sach if kiem_tra_nguyen_to(x))
print("Số lượng số nguyên tố:", so_nguyen_to)

trung_binh = sum(danh_sach) / len(danh_sach)
print("Giá trị trung bình:", trung_binh)
