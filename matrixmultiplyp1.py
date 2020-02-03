#Jessica Redekop
#Parallel Programming Assignment 1 Part 1
#Feb 2, 2020

import matrixUtils
import time

size = 256
matrix_1 = matrixUtils.genMatrix(size,2)
matrix_2 = matrixUtils.genMatrix2(size,3)
matrix_2_transpose = [[row[i] for row in matrix_2] for i in range(len(matrix_2[0]))]
            
matrix_sol = [[0] * size for i in range(size)]

for i in range(size):
    for j in range(size):
        for k in range(size):
            matrix_sol[i][j] += matrix_1[i][k] * matrix_2[k][j]
        
start = time.time()
stop = time.time() - start
print("time: ")
print(stop)
print("\n")

print(matrix_sol)
