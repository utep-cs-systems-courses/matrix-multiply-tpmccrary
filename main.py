# Author: Timothy P. McCrary

from typing import List
from matrix_multiply import matrixUtils
from matrix_multiply.matrix_multiplication import MatrixMultiplication
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
    # Implement parallel matrix multiply. Use examples with 1, 2, 4, and 8 threads. DONE

    # Matrices that will be used for testing.
    matrix_1: List[List[int]] = matrixUtils.readFromFile("test/matrix_550x550_5")
    matrix_2: List[List[int]] = matrixUtils.readFromFile("test/matrix_550x550_10")

    run_parallel_matrix_multiply(matrix_1, matrix_2, 1)
    run_parallel_matrix_multiply(matrix_1, matrix_2, 2)
    run_parallel_matrix_multiply(matrix_1, matrix_2, 4)
    run_parallel_matrix_multiply(matrix_1, matrix_2, 8)

    

def run_parallel_matrix_multiply(matrix_1, matrix_2, num_threads):
    print(f"Multiplying: {len(matrix_1)}x{len(matrix_1[0])} matrix, values = {matrix_1[0][0]} WITH {len(matrix_2)}x{len(matrix_2[0])} matrix, values = {matrix_2[0][0]}.")
    print(f"Using {num_threads} thread(s).")

    startTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    matrixUtils.printSubarray(MatrixMultiplication.parallel_matrix_multiply(matrix_1, matrix_2, num_threads))
    endTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    elapsedTime: float = endTime - startTime

    print(f"Duration: {elapsedTime}s\n")




if __name__ == '__main__':
    main()

