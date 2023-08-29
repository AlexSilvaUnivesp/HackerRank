import numpy as np

arr = [[1, 1, 1, 0, 0, 0],
[0, 4, 0, 0, 0, 7],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]

matrix = np.array(arr)

max_sum = 0
for i in range(4):
    for j in range(4):
        sub_matrix = matrix[i:i+3, j:j+3]
        left = np.sum(matrix[i+1:i+2, j:j+1])
        right = np.sum(matrix[i+1:i+2, j+2:j+3])
        soma = np.sum(sub_matrix) - left - right
        if soma > max_sum: max_sum = soma

print(max_sum)