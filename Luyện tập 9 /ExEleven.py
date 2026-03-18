print("--- CHẠY BÀI 11 ---")
class SinhVien:
    so_luong = 0  

    def __init__(self, diem):
        self.diem = diem
        SinhVien.so_luong += 1  

    @classmethod
    def dem_sinh_vien(cls):
        return cls.so_luong

print("--- KẾT QUẢ BÀI 11 ---")
sv_a = SinhVien(7)
sv_b = SinhVien(8)
sv_c = SinhVien(10)
