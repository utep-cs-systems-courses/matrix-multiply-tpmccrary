from typing import List
import pymp

class MatrixMultiplication:
    '''Handles matrix multiplication. Used as a static class.
    '''

    def scalar_multiply(matrix_1: List[List[int]], scalar_num: int = 1) -> List[List[int]]:
        '''Multiplies a given matrix by a given scalar integer.

        Args:
            matrix_1 (List[List[int]]): The given matrix.
            scalar_num (int): The given scalar integer.

        Returns:
            List[List[int]]: The product of the scalar multiplication
        '''
        
        matrix_product: List[List[int]] = []

        # Go through every row in the given matrix.
        row: List[int]
        for row in matrix_1:
            product_row: List[int] = []

            # In the matrix row, go through every element.
            element: int
            for element in row:
                # Multiply each element by the scalar num and add it to a new list.
                product_row.append(element * scalar_num)
            
            # Append the newely populated list to a new matrix. 
            matrix_product.append(product_row)

        return matrix_product

    def matrix_multiply(matrix_1: List[List[int]], matrix_2: List[List[int]]) -> List[List[int]]:
        '''Given two matrices, multiplies them and returns their product.
        Note: The number of columns in matrix 1 must be equal to the number of row in matrix 2.

        Args:
            matrix_1 (List[List[int]]): The first given matrix.
            matrix_2 (List[List[int]]): The second given matrix.

        Returns:
            List[List[int]]: The matrix product.
        '''

        # Get the row and col sizes for the matrices to be used for later.
        matrix_1_num_row: int = len(matrix_1)
        matrix_1_num_col: int = len(matrix_1[0])
        # matrix_2_num_row: int = len(matrix_2) 
        matrix_2_num_col: int = len(matrix_2[0])

        # Create a new matrix with the correct size.
        matrix_product: List[List[int]] = [[None] * matrix_2_num_col] * matrix_1_num_row

        # Check to make sure the number of cols in the first matrix equals the number of rows in the second matrix.
        if (len(matrix_1[0]) != len(matrix_2)):
            print("ERROR: The number of columns in matrix 1 does not equal the number of rows in matrix 2.\nCANNOT MULTIPLY")
            return matrix_product

        # Go through each row in matrix 1.
        for i in range(matrix_1_num_row):
            # Go through each column in matrix 2.
            for j in range (matrix_2_num_col):
                dot_product: int = 0
                # Since matrix 1 col == matrix 2 row, we use k to iterate thorugh matrix 1 col and matrix 2 row respectively.
                for k in range(matrix_1_num_col):
                    dot_product = (matrix_1[i][k] * matrix_2[k][j]) + dot_product
                
                # Store the dot product in the new matrix.
                matrix_product[i][j] = dot_product


        return matrix_product

    def matrix_blocked_multiply(matrix_1: List[List[int]], matrix_2: List[List[int]], tile_size: int) -> List[List[int]]:
        
        matrix_product: List[List[int]] = [[0] * len(matrix_2[0])] * len(matrix_1)

        for kk in range(len(matrix_1)):
            for jj in range(len(matrix_2)):
                for i in range(len(matrix_1)):
                    j_end_val = jj + tile_size

                    for j in range(jj, j_end_val):
                        k_end_val = kk + tile_size

                        sum = matrix_product[i][j]

                        for k in range(kk, k_end_val):
                            sum = sum + matrix_1[i][k] * matrix_2[k][j]
                        
                        matrix_product[i][j] = sum


        return matrix_product


    def parallel_matrix_multiply(matrix_1: List[List[int]], matrix_2: List[List[int]], num_threads: int) -> List[List[int]]:
        '''Given two matrices, multiplies them and returns their product.
        Note: The number of columns in matrix 1 must be equal to the number of row in matrix 2.

        Args:
            matrix_1 (List[List[int]]): The first given matrix.
            matrix_2 (List[List[int]]): The second given matrix.

        Returns:
            List[List[int]]: The matrix product.
        '''

        # Get the row and col sizes for the matrices to be used for later.
        matrix_1_num_row: int = len(matrix_1)
        matrix_1_num_col: int = len(matrix_1[0])
        # matrix_2_num_row: int = len(matrix_2) 
        matrix_2_num_col: int = len(matrix_2[0])

        # Create a new matrix with the correct size.
        # matrix_product: List[List[int]] = [[None] * matrix_2_num_col] * matrix_1_num_row
        matrix_product = pymp._shared.array((matrix_2_num_col, matrix_1_num_row), int)
        assigned_start: List = pymp._shared.list()

        

        # Check to make sure the number of cols in the first matrix equals the number of rows in the second matrix.
        if (len(matrix_1[0]) != len(matrix_2)):
            print("ERROR: The number of columns in matrix 1 does not equal the number of rows in matrix 2.\nCANNOT MULTIPLY")
            return matrix_product

        
        with pymp.Parallel(num_threads) as p:

            product_lock = p.lock

            # Go through each row in matrix 1.
            for i in p.range(0, matrix_1_num_row):
                
                # Go through each column in matrix 2.
                for j in range (matrix_2_num_col):
                    dot_product: int = 0
                    # Since matrix 1 col == matrix 2 row, we use k to iterate thorugh matrix 1 col and matrix 2 row respectively.
                    for k in range(matrix_1_num_col):
                        dot_product = (matrix_1[i][k] * matrix_2[k][j]) + dot_product
                    
                    product_lock.acquire()
                    # Store the dot product in the new matrix.
                    matrix_product[i][j] = dot_product
                    product_lock.release()


        return matrix_product

