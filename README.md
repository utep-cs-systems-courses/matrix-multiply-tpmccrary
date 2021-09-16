# Matrix Multiply

Matrix Multiplly is a Python program that implements matrix multiplication without the use of external libraries.<br/>
Additionally, a parallel algorithm has been implemented to speed up the process.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `numpy` and `pymp`.

```bash
pip install numpy
```
```bash
pip install pymp-pypi
```

## Usage

This program uses a CLI (commnad line interface) to recieve user input.<br/><br/>
Use the following commands in the root folder of the program.<br/>
For CLI help:
```bash
python3 main.py -h
```
Example usage running hard-coded parallel algorithm test:
```bash
python3 main.py -pt
```

# Report
## Part 2

## Part 1
Implementing the matrix multiplication functionality was straight forward and uses a simple nested "for loop" algorithm. Although, it was important to follow the mathematical constraints (like matrix 1 must have the same number of col as rows in matrix 2).<br/> 
It is important to note, UI functionality is not incorporated. As of now, this program is meant to test matrixes that are already generated and show the matrix multiplication functionality working. The actual matrix multiplication functions can be found in the file `matrix_multiply/matrix_multiplication.py` in the `MatrixMultiplication` class. This class contains two functions: `scalar_multiply` and `matrix_multiply`, where the actual multiplication is done.<br/>
In order to time the program, `timeit` is used, however, when this program becomes parallel, that will be changed to a more robust system.<br/> 
One thing worth noting, the time it takes to mutliply matrices with sizes of at least 500x500 take longer than 15 seconds. Futhermore, matrices with sizes above 1000 take unnecessary amount of time as a serial program. I expect with a parallel implementation, speeds will drastically increase.

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5458401&assignment_repo_type=AssignmentRepo)
