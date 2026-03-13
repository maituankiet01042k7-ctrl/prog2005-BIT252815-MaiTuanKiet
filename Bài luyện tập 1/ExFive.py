# ==================== BÀI 5 ====================
print("\n--- Bài 5 ---")
M = int(input("Nhập số hàng M: "))
N = int(input("Nhập số cột N: "))

ma_tran = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]

print("Ma trận đã khởi tạo:")
for hang in ma_tran:
    print(hang)

chon_hang = int(input(f"Yêu cầu hiển thị hàng (0 đến {M-1}): "))
if 0 <= chon_hang < M:
    print(f"Dữ liệu hàng {chon_hang}:", ma_tran[chon_hang])
else:
    print("Chỉ số hàng không hợp lệ!")

chon_cot = int(input(f"Yêu cầu hiển thị cột (0 đến {N-1}): "))
if 0 <= chon_cot < N:
    cot_data = [ma_tran[i][chon_cot] for i in range(M)]
    print(f"Dữ liệu cột {chon_cot}:", cot_data)
else:
    print("Chỉ số cột không hợp lệ!")

max_val = max(max(hang) for hang in ma_tran)
print("Giá trị lớn nhất trong ma trận:", max_val)
