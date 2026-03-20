import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Bài 3
# ==========================================
san_pham = ['A', 'B', 'C', 'D', 'E']
doanh_so = [30, 25, 15, 20, 10]

plt.figure(figsize=(7, 7))
plt.pie(doanh_so, labels=san_pham, autopct='%1.0f%%', startangle=140)
plt.title('Tỷ lệ phần trăm doanh số của 5 sản phẩm')
plt.show()
