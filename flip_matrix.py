import numpy as np

arr = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
matrix = np.array(arr)
n = len(matrix)
total = 0
for i in range(n//2):
    for j in range(n//2):
        subtotal = max(matrix[i][j], matrix[i][n-1-j], matrix[n-1-i][j], matrix[n-1-i][n-1-j])
        total += subtotal

print(total)
