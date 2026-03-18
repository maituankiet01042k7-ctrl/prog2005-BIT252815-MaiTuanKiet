class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    # Nạp chồng toán tử == (so sánh bằng)
    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False

# ----- CHẠY THỬ BÀI 10 -----
print("--- KẾT QUẢ BÀI 10 ---")
sv1 = SinhVien(8.5)
sv2 = SinhVien(8.5)
sv3 = SinhVien(9.0)

print(f"Điểm sv1 (8.5) có bằng sv2 (8.5) không? -> {sv1 == sv2}")
print(f"Điểm sv1 (8.5) có bằng sv3 (9.0) không? -> {sv1 == sv3}")
