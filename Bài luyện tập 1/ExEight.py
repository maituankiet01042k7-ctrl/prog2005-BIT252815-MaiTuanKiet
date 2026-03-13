# ==================== BÀI 8 ====================
print("\n--- Bài 8 ---")
class Student_B8:
    def __init__(self, ten, diem):
        self.ten = ten
        if 0 <= diem <= 10:
            self.diem = diem
            print(f"Khởi tạo thành công: Điểm của {self.ten} hợp lệ ({self.diem}).")
        else:
            self.diem = 0 
            print(f"Lỗi: Điểm của {self.ten} ({diem}) không hợp lệ! Điểm phải từ 0 đến 10.")

sv3 = Student_B8("Le Van C", 11)  
sv4 = Student_B8("Pham Thi D", 7) 
