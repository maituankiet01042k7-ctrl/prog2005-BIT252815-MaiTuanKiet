# BÀI 7
def tinh_diem_trung_binh(students_dict):
    if not students_dict:
        return 0
    return sum(students_dict.values()) / len(students_dict)

def bai_7():
    students = {
        "Nguyen Van An": 8.5,
        "Tran Thi Binh": 7.0,
        "Le Van Chuong": 9.0
    }
    print(f"Danh sách sinh viên: {students}")
    print(f"Điểm trung bình của các sinh viên: {tinh_diem_trung_binh(students):.2f}")

if __name__ == "__main__":
    bai_7()
