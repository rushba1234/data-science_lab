import numpy

matrix1 = numpy.matrix([[1, 2, 3], [1, 1, 1], [1, 1, 1]])

matrix2 = numpy.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print("Matrix 1=\n", matrix1)
print("Matrix 2=\n", matrix2)

matrix3 = numpy.add(matrix1, matrix2)
matrix4 = numpy.subtract(matrix1, matrix2)
matrix5 = numpy.matmul(matrix1, matrix2)
matrix6 = numpy.transpose(matrix1)

print("Matrix 1 + Matrix 2=\n", matrix3)
print("Matrix 1 - Matrix 2=\n", matrix4)
print("Matrix 1 * Matrix 2=\n", matrix5)
print("2 * Matrix 1=\n", 2 * matrix1)
print("Transpose of Matrix 1=\n", matrix6)
