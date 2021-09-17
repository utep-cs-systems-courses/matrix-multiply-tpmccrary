# Matrix Multiply

Matrix Multiplly is a Python program that implements matrix multiplication without the use of external libraries.<br/>
Additionally, a parallel algorithm has been implemented to speed up the process. <br/>
### NOTE: Report can be found at bottom of README.

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
Outputting:
```
Perform matrix multiplication on given files.

optional arguments:
  -h, --help            show this help message and exit
  -pt, --parallel_test  Run parallel tests?
  -f, --forloop         Use 3 nested for loops algorithm.
  -p, --parallel        Use parallel algorithm.
  -nt NUM_THREAD, --num_thread NUM_THREAD
                        (int, optional) Number of threads to use in parallel.
  -f1 FILE1, --file1 FILE1
                        (str, optional) File path of first matrix to use.
  -f2 FILE2, --file2 FILE2
                        (str, optional) File path of second matrix to use.
```
### Example usage running hard-coded parallel algorithm test <br/>(recommneded for quick use, without the need for configuration):
```bash
python3 main.py -pt
```

# Report
## Part 2
#### Problems
When coding for part 2 of this assignemnt, I enountered one problem. At first, I used a regular variable and forgot to use a explicitly delcared shared variable. This lead to me getting the incorrect results from the parallel matrix multiplication algorithm, as all the threads were accessing their own matrix in memory. All that needed to be done was to declare a shared variable through `pymp`, which allowed all the threads to access that single matrix and return the correct result.
#### Time to Complete
In all, it took around 4 to 5 hours to complete part 2. After understanding how `pymp` works with the use of the provided examples and cheat sheat, I was able to understand how all the pieces "fit together".
#### Performance Measurements
This program was tested using 550x550 matrices using 1, 2, 4, and 8 threads. 

1 Thread: `9.171762600000001s`<br/>
2 Threads: `4.8797151s`<br/>
4 Threads: `2.4673986999999986s`<br/>
8 Threads: `1.3943424000000029s`<br/>

Overall, throwing more threads at this problem reduced the duration of the algorithm. It seems doubling the threads halfs the time it takes for the algorith to complete.

### Analysis
Before explaing why this speeds up the algorithm, I must first describe how it is implemented. This algorihtm uses 3 nested for loops; first loop for going through matrix 1 rows, second for matrix 2 columns, and third for the resulting matrix elements. This algorithm was parallelized by breaking up the row operations in matrix 1. So, instead of the algorithm going row by row, the rows are broken up, and "handed out" to different threads. For example on a 10x10 matrix, the non-parallel algorithm would start at row 1, and increment to row 10, doing the needed computations along the way. The parallel algorithm distributes the work so, say, thread 1 would get rows 1 to 3, thread 2 gets rows 4 to 6, thread 3 gets 7 to 10. This breaks up the computation so they are all happening at the same time, decreasing the duration drastically, especially compared to going one at a time. 

### CPU Info
```
model name	: AMD Ryzen 7 5800H with Radeon Graphics
     16     160     832
```
## Part 1
Implementing the matrix multiplication functionality was straight forward and uses a simple nested "for loop" algorithm. Although, it was important to follow the mathematical constraints (like matrix 1 must have the same number of col as rows in matrix 2).<br/> 
It is important to note, UI functionality is not incorporated. As of now, this program is meant to test matrixes that are already generated and show the matrix multiplication functionality working. The actual matrix multiplication functions can be found in the file `matrix_multiply/matrix_multiplication.py` in the `MatrixMultiplication` class. This class contains two functions: `scalar_multiply` and `matrix_multiply`, where the actual multiplication is done.<br/>
In order to time the program, `timeit` is used, however, when this program becomes parallel, that will be changed to a more robust system.<br/> 
One thing worth noting, the time it takes to mutliply matrices with sizes of at least 500x500 take longer than 15 seconds. Futhermore, matrices with sizes above 1000 take unnecessary amount of time as a serial program. I expect with a parallel implementation, speeds will drastically increase.

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5458401&assignment_repo_type=AssignmentRepo)
