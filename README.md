# About
This Python program is an implementation of matrix multiplication, without using external libraries.<br/>
As a test, this program will automatically use two matrices and multiply them together.

# Instructions to Run
In the project root directory, use the command:
```python3 main.py```

# Report
## Part 2

## Part 1
Implementing the matrix multiplication functionality was straight forward and uses a simple nested "for loop" algorithm. Although, it was important to follow the mathematical constraints (like matrix 1 must have the same number of col as rows in matrix 2).<br/> 
It is important to note, UI functionality is not incorporated. As of now, this program is meant to test matrixes that are already generated and show the matrix multiplication functionality working. The actual matrix multiplication functions can be found in the file `matrix_multiply/matrix_multiplication.py` in the `MatrixMultiplication` class. This class contains two functions: `scalar_multiply` and `matrix_multiply`, where the actual multiplication is done.<br/>
In order to time the program, `timeit` is used, however, when this program becomes parallel, that will be changed to a more robust system.<br/> 
One thing worth noting, the time it takes to mutliply matrices with sizes of at least 500x500 take longer than 15 seconds. Futhermore, matrices with sizes above 1000 take unnecessary amount of time as a serial program. I expect with a parallel implementation, speeds will drastically increase.

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5458401&assignment_repo_type=AssignmentRepo)
