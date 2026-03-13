# ==================== BÀI 7 ====================
print("--- Bài 7 ---")
class Student_B7:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

sv1 = Student_B7("Nguyen Van A", 8.5)
sv2 = Student_B7("Tran Thi B", 9.0)

print(f"Đã khởi tạo sinh viên 1: Tên = {sv1.ten}, Điểm = {sv1.diem}")
print(f"Đã khởi tạo sinh viên 2: Tên = {sv2.ten}, Điểm = {sv2.diem}")
