import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Bài 4
# ==========================================
data = {
    'City': ['Los Angeles', 'San Diego', 'California City', 'San Jose', 'Bakersfield',
             'Fresno', 'Palmdale', 'Sacramento', 'Lancaster', 'San Francisco', 'Santa Ana'],
    'area_total_km2': [1302.15, 964.51, 527.40, 461.96, 389.60,
                       297.41, 275.10, 259.27, 244.98, 121.40, 70.62]
}
df = pd.DataFrame(data)

df_top10 = df.sort_values(by='area_total_km2', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(df_top10['City'], df_top10['area_total_km2'], color='lightgreen')
plt.gca().invert_yaxis()
plt.title('Top 10 thành phố lớn nhất theo diện tích ở California')
plt.xlabel('Diện tích (km²)')
plt.ylabel('Thành phố')
plt.show()
