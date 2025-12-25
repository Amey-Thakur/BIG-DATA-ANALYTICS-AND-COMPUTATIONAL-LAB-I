#!/usr/bin/env python
"""
Matrix Multiplication using MapReduce - Mapper

Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
Course: Big Data Analytics & Computational Lab -I (BDA&CL-I)
Experiment 5: Matrix Multiplication using MapReduce
Date: October 5, 2021
Repository: https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I

Description:
This mapper script processes two input matrices and generates intermediate key-value pairs
for matrix multiplication using the MapReduce paradigm. The mapper reads matrix elements
from standard input and emits tuples (row, col, source, value) for the reducer to aggregate.

Matrix Dimensions:
- Matrix 1 (m): 2 rows x 3 columns
- Matrix 2 (n): 3 rows x 2 columns
- Result Matrix: 2 rows x 2 columns
"""

import sys

# Matrix dimensions
m_r = 2  # Number of rows in matrix 1
m_c = 3  # Number of columns in matrix 1
n_r = 3  # Number of rows in matrix 2
n_c = 2  # Number of columns in matrix 2

i = 0  # Line counter to distinguish between matrices

# Read input line by line
for line in sys.stdin:
    # Convert line elements to integers
    el = map(int, line.split())
    
    # Process Matrix 1 (first m_r rows)
    if(i < m_r):
        # For each element in the row
        for j in range(len(el)):
            # For each column in result matrix
            for k in range(n_c):
                # Emit: result_row, result_col, source_col/row, value
                # Format: (i, k, j, el[j])
                # where i = result row, k = result col, j = matrix1 col, el[j] = value
                print('%d\t%d\t%d\t%d' %(i, k, j, el[j]))
    
    # Process Matrix 2 (remaining rows)
    else:
        # For each element in the row
        for j in range(len(el)):
            # For each row in result matrix
            for k in range(m_r):
                # Emit: result_row, result_col, source_col/row, value
                # Format: (k, j, i+m_r, el[j])
                # where k = result row, j = result col, i+m_r = matrix2 row, el[j] = value
                print('%d\t%d\t%d\t%d' %(k, j, i + m_r, el[j]))
    
    # Increment line counter
    i = i + 1
