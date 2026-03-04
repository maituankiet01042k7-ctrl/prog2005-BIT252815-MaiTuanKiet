#Bai 12:
matrix_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_B = [
    [7, 8, 9],
    [10, 11, 12]
]

m = len(matrix_A)
n = len(matrix_A[0])

result_matrix = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        result_matrix[i][j] = matrix_A[i][j] + matrix_B[i][j]

print("Ma trận kết quả sau khi cộng:")
for row in result_matrix:
    print(row)
