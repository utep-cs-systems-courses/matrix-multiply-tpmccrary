# Author: Timothy P. McCrary

from matrix_multiply import matrixUtils
from matrix_multiply.matrix_multiplication import MatrixMultiplication
from timeit import default_timer

def main():

    # TODO:
    # Multiply matrixes. DONE
    # Print small portion of matrix. DONE
    # Time how long it takes to complete matrix multiply. DONE
    # Include instructions on how to run program. DONE
    # Submit through github.
    # Use large enough matrices so that it takes around 10s. DONE

    print("Multiplying a 450x450 matrix with values of 5 with another 450x450 matrix with values of 10:")
    start = default_timer()
    matrixUtils.printSubarray(MatrixMultiplication.matrix_multiply(matrixUtils.readFromFile("test/matrix_450x450_5"), matrixUtils.readFromFile("test/matrix_450x450_10")))
    duration = default_timer() - start
    print("Duration: " + str(duration) + "(s)")


    print("Multiplying two random 450x450 matrices:")
    start = default_timer()
    matrixUtils.printSubarray(MatrixMultiplication.matrix_multiply(matrixUtils.readFromFile("test/matrix_450x450_rand1"), matrixUtils.readFromFile("test/matrix_450x450_rand2")))
    duration = default_timer() - start
    print("Duration: " + str(duration) + "(s)")


if __name__ == '__main__':
    main()

