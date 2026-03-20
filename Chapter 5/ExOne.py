import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Bài 1
# ==========================================
ket_qua = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
so_luong = [6, 10, 12, 4, 1]

plt.figure(figsize=(8, 5))
plt.bar(ket_qua, so_luong, color='skyblue')
plt.title('Kết quả học tập của lớp')
plt.xlabel('Xếp loại học lực')
plt.ylabel('Số lượng học sinh')
plt.show()
