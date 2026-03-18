print("--- CHẠY BÀI 10 ---")
class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False

print("--- KẾT QUẢ BÀI 10 ---")
sv1 = SinhVien(8.5)
sv2 = SinhVien(8.5)
sv3 = SinhVien(9.0)

print(f"Điểm sv1 (8.5) có bằng sv2 (8.5) không? -> {sv1 == sv2}")
print(f"Điểm sv1 (8.5) có bằng sv3 (9.0) không? -> {sv1 == sv3}")
