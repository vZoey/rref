from sympy import *

print("The row size is the vertical size of the matrix, and the column size is the horizontal size of the matrix.")

matrixRSize = int(input("Enter the matrix row size: "))
matrixCSize = int(input("Enter the matrix column size: "))

matrix = Matrix(matrixRSize, matrixCSize, lambda i, j: int(input("Enter the value at row " + str(i + 1) + " and column " + str(j + 1) + ": ")))
answer = matrix.rref()
print(str(answer).strip("Matrix([[").strip("]])").strip("]) ( 0 1").strip(") (0,").replace("], [", "\n").replace(", ", " ").replace("]]", "]"))