# Author: Timothy P. McCrary

from typing import List
from matrix_multiply import matrixUtils
from matrix_multiply.matrix_multiplication import MatrixMultiplication
from timeit import default_timer
import time

def main():

    # TODO:
    # Multiply matrixes. DONE
    # Print small portion of matrix. DONE
    # Time how long it takes to complete matrix multiply. DONE
    # Include instructions on how to run program. DONE
    # Submit through github.
    # Use large enough matrices so that it takes around 10s. DONE
    # Add more detail to report, including where the matrix multiplication functions are found. DONE
    # Implement block matrix multiply. Aglorithm can be found on onenote. DONE
    # Implement parallel matrix multiply. Use examples with 1, 2, 4, and 8 threads.

    matrix_1: List[List[int]] = matrixUtils.readFromFile("test/matrix_450x450_5")
    matrix_2: List[List[int]] = matrixUtils.readFromFile("test/matrix_450x450_10")

    print("Multiplying a 450x450 matrix with values of 5 with another 450x450 matrix with values of 10:")
    startTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    matrixUtils.printSubarray(MatrixMultiplication.matrix_multiply(matrix_1, matrix_2))
    endTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    elapsedTime: float = endTime - startTime
    print(f"Duration: {elapsedTime}s")

    return
    

    print("Multiplying a 450x450 matrix with values of 5 with another 450x450 matrix with values of 10:")
    start = default_timer()
    matrixUtils.printSubarray(MatrixMultiplication.matrix_multiply(matrixUtils.readFromFile("test/matrix_450x450_5"), matrixUtils.readFromFile("test/matrix_450x450_10")))
    duration = default_timer() - start
    print("Duration: " + str(duration) + "(s)")

    print("Blocked multiplying a 450x450 matrix with values of 5 with another 450x450 matrix with values of 10:")
    start = default_timer()
    matrixUtils.printSubarray(MatrixMultiplication.matrix_blocked_multiply(matrixUtils.readFromFile("test/matrix_450x450_5"), matrixUtils.readFromFile("test/matrix_450x450_10"), 25))
    duration = default_timer() - start
    print("Duration: " + str(duration) + "(s)")

    print("Multiplying two random 450x450 matrices:")
    start = default_timer()
    matrixUtils.printSubarray(MatrixMultiplication.matrix_multiply(matrixUtils.readFromFile("test/matrix_450x450_rand1"), matrixUtils.readFromFile("test/matrix_450x450_rand2")))
    duration = default_timer() - start
    print("Duration: " + str(duration) + "(s)")




if __name__ == '__main__':
    main()

