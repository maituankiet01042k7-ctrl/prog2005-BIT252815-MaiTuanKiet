class User:
    def __init__(self, user_id):
        self._id = user_id

    @property 
    def id(self): 
        return self._id

print("--- KẾT QUẢ BÀI 5 ---")
nguoi_dung = User("SV_CMC_001")
print(f"ID của người dùng là: {nguoi_dung.id}")
print("---------------------")
