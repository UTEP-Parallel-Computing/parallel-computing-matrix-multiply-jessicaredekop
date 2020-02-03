#Jessica Redekop
#Parallel Programming Assignment 1 Part 1
#Feb 2, 2020

import matrixUtils
import time

#making size of quare matrix modular
size = 256

#generating matricies using the utils
matrix_1 = matrixUtils.genMatrix(size,2)
matrix_2 = matrixUtils.genMatrix2(size,3)
#creating a same size matrix filled with 0s 
matrix_sol = [[0] * size for i in range(size)]

#starting timer
start = time.time()

#nested for loops because I don't understand the syntax for python list comprehension
for i in range(size):
    for j in range(size):
        for k in range(size):
            matrix_sol[i][j] += matrix_1[i][k] * matrix_2[k][j]
        
#stopping timer
stop_time = time.time() - start

print("time: ")
print("%s seconds" % stop_time)
print("\n")

#print solution
matrixUtils.printSubarray(matrix_sol)