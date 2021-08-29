from typing import List

class MatrixMultiplication:
    '''Handles matrix multiplication.
    '''

    def __init__(self) -> None:
        pass

    def scalar_multiply(matrix_1: List[List[int]], scalar_num: int) -> List[List[int]]:
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

