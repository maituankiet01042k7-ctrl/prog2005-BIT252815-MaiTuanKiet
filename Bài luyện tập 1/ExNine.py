# ==================== BÀI 9 ====================
print("\n--- Bài 9 ---")
class Student_B9:
    def __init__(self, ten, diem):
        self.ten = ten
        if 0 <= diem <= 10:
            self.diem = diem
        else:
            self.diem = 0 
            
    def display(self):
        if self.diem.is_integer() if isinstance(self.diem, float) else True:
            print(f"Sinh viên {self.ten} có điểm là {int(self.diem)}")
        else:
            print(f"Sinh viên {self.ten} có điểm là {self.diem}")

sv5 = Student_B9("A", 10)
sv5.display()
