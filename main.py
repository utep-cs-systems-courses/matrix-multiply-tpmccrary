# Author: Timothy P. McCrary

from matrix_multiply import matrixUtils
from matrix_multiply.matrix_multiplication import MatrixMultiplication

def main():
    print("Hello World!")

    # TODO:
    # Multiply matrixes.
    # Print small portion of matrix.
    # Time how long it takes to complete matrix multiply.
    # Include instructions on how to run program.
    # Submit through github.
    # Use large enough matrices so that it takes around 10s.

    print(MatrixMultiplication.scalar_multiply(matrixUtils.genMatrix2(100, 5), 10))

    pass

if __name__ == '__main__':
    main()