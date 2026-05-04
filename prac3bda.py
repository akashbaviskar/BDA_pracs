#Prac3 Implement Matrix Multiplication using Map-Reduce 
from collections import defaultdict
# Input matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]
mapped = []
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            mapped.append(((i, j), A[i][k] * B[k][j]))
            
result = defaultdict(int)

for key, value in mapped:
    result[key] += value

rows = len(A)
cols = len(B[0])

print("Result Matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(result[(i, j)])
    print(row)
#-------------x-----------------