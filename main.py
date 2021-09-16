# Author: Timothy P. McCrary

from argparse import ArgumentParser
from typing import List

from pymp import Parallel
from matrix_multiply import matrixUtils
from matrix_multiply.matrix_multiplication import MatrixMultiplication
import time


def main():

    # TODO:
    # Multiply matrices. DONE
    # Print small portion of matrix. DONE
    # Time how long it takes to complete matrix multiply. DONE
    # Include instructions on how to run program. DONE
    # Submit through github. DONE
    # Use large enough matrices so that it takes around 10s. DONE
    # Add more detail to report, including where the matrix multiplication functions are found. DONE
    # Implement block matrix multiply. Aglorithm can be found on onenote. DONE
    # Implement parallel matrix multiply. Use examples with 1, 2, 4, and 8 threads. DONE

    parser: ArgumentParser = ArgumentParser(
        description='Perform matrix multiplication on given files.')
    parser.add_argument('-pt', '--parallel_test', action="store_true",
                    help='Run parallel tests?')
    parser.add_argument('-f', '--forloop', action="store_true",
                        help='Use 3 nested for loops algorithm.')
    parser.add_argument('-p', '--parallel', action="store_true",
                        help='Use parallel algorithm.')
    parser.add_argument('-nt', '--num_thread', default=1, type=int,
                        help='(int, optional) Number of threads to use in parallel.')
    parser.add_argument('-f1', '--file1', default="test/matrix_550x550_5", type=str,
                        help='(str, optional) File path of first matrix to use.')
    parser.add_argument('-f2', '--file2', default="test/matrix_550x550_10", type=str,
                        help='(str, optional) File path of second matrix to use.')
    

    args = parser.parse_args()

    use_forloop: bool = args.forloop
    use_parallel: bool = args.parallel
    use_parallel_tests: bool = args.parallel_test
    num_threads: int = args.num_thread
    matrix_1_filename: str = args.file1
    matrix_2_filename: str = args.file2

    # Matrices that will be used for testing.
    matrix_1: List[List[int]] = matrixUtils.readFromFile(
        matrix_1_filename)
    matrix_2: List[List[int]] = matrixUtils.readFromFile(
        matrix_2_filename)

    if (use_parallel == True):
        run_parallel_matrix_multiply(matrix_1, matrix_2, num_threads)
    elif (use_forloop == True):
        run_matrix_multiply(matrix_1, matrix_2)
    elif (use_parallel_tests == True):
        run_parallel_matrix_multiply(matrix_1, matrix_2, 1)
        run_parallel_matrix_multiply(matrix_1, matrix_2, 2)
        run_parallel_matrix_multiply(matrix_1, matrix_2, 4)
        run_parallel_matrix_multiply(matrix_1, matrix_2, 8)
    else:
        print("Do: \"python3 main.py -h\" for help.")
        # run_parallel_matrix_multiply(matrix_1, matrix_2, num_threads)

    


def run_parallel_matrix_multiply(matrix_1: List[List[int]], matrix_2: List[List[int]], num_threads: int):
    """Given two matrices, and a thread amount, calls parallel matrix multiply and prints the results.

    Args:
        matrix_1 (List[List[int]]): Matrix that will be multiplied.
        matrix_2 (List[List[int]]): Matrix that will be multiplied.
        num_threads (int): Number of threads that will be used for parallel matrix multiplication.
    """
    print(f"Parallel multiplying: {len(matrix_1)}x{len(matrix_1[0])} matrix, values = {matrix_1[0][0]} WITH {len(matrix_2)}x{len(matrix_2[0])} matrix, values = {matrix_2[0][0]}.")
    print(f"Using {num_threads} thread(s).")

    startTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    matrix_product: List[List[int]] = MatrixMultiplication.parallel_matrix_multiply(
        matrix_1, matrix_2, num_threads)
    matrixUtils.printSubarray(matrix_product)
    endTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    elapsedTime: float = endTime - startTime

    print(f"Duration: {elapsedTime}s\n")

def run_matrix_multiply(matrix_1: List[List[int]], matrix_2: List[List[int]]):
    print(f"Multiplying: {len(matrix_1)}x{len(matrix_1[0])} matrix, values = {matrix_1[0][0]} WITH {len(matrix_2)}x{len(matrix_2[0])} matrix, values = {matrix_2[0][0]}.")

    startTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    matrix_product: List[List[int]] = MatrixMultiplication.matrix_multiply(
        matrix_1, matrix_2)
    matrixUtils.printSubarray(matrix_product)
    endTime: float = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    elapsedTime: float = endTime - startTime

    print(f"Duration: {elapsedTime}s\n")


if __name__ == '__main__':
    main()
