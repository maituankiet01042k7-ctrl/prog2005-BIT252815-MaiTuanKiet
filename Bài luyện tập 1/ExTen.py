# ==================== BÀI 10 ====================
print("\n--- Bài 10 ---")
ten_file = "sanpham.txt"

print("Nhập thông tin sản phẩm (Nhấn Enter ở Mã sản phẩm để dừng nhập):")
while True:
    ma_sp = input("Mã sản phẩm (Code): ").strip()
    if not ma_sp:
        break
    ten_sp = input("Tên sản phẩm (Name): ").strip()
    gia_sp = float(input("Giá (Price): "))
    
    with open(ten_file, "a", encoding="utf-8") as f:
        f.write(f"{ma_sp};{ten_sp};{gia_sp}\n")

danh_sach_sp = []
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        print("\n=== Danh sách sản phẩm từ tệp ===")
        for dong in f:
            dong = dong.strip()
            if dong:
                print(dong)
                thong_tin = dong.split(";")
                if len(thong_tin) == 3:
                    danh_sach_sp.append({
                        "ma": thong_tin[0],
                        "ten": thong_tin[1],
                        "gia": float(thong_tin[2])
                    })
                
    print("\n=== Danh sách sản phẩm sắp xếp theo giá giảm dần ===")
    danh_sach_sp.sort(key=lambda x: x["gia"], reverse=True)
    for sp in danh_sach_sp:
        if sp['gia'].is_integer():
            print(f"{sp['ma']};{sp['ten']};{int(sp['gia'])}")
        else:
            print(f"{sp['ma']};{sp['ten']};{sp['gia']}")
        
except FileNotFoundError:
    print("Tệp không tồn tại hoặc chưa có dữ liệu.")
