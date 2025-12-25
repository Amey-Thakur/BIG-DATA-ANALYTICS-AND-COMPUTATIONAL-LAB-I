#!/usr/bin/env python
"""
Matrix Multiplication using MapReduce - Reducer

Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
Course: Big Data Analytics & Computational Lab -I (BDA&CL-I)
Experiment 5: Matrix Multiplication using MapReduce
Date: October 5, 2021
Repository: https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I

Description:
This reducer script aggregates the intermediate key-value pairs emitted by the mapper
to compute the final matrix multiplication result. It reads sorted mapper output from
standard input and performs element-wise multiplication and summation to produce the
resultant matrix.

Matrix Dimensions:
- Matrix 1 (m): 2 rows x 3 columns
- Matrix 2 (n): 3 rows x 2 columns
- Result Matrix: 2 rows x 2 columns
"""

import sys

# Matrix dimensions
m_r = 2  # Number of rows in matrix 1 (also rows in result matrix)
m_c = 3  # Number of columns in matrix 1 (also rows in matrix 2)
n_r = 3  # Number of rows in matrix 2
n_c = 2  # Number of columns in matrix 2 (also columns in result matrix)

# Initialize result matrix
matrix = []

# Build the result matrix by iterating through each position
for row in range(m_r):
    r = []  # Current row of result matrix
    
    for col in range(n_c):
        s = 0  # Sum for current cell (row, col)
        
        # Compute dot product of row from Matrix 1 and column from Matrix 2
        for el in range(m_c):
            mul = 1  # Product of corresponding elements
            
            # Read two lines from mapper output (one from each matrix)
            for num in range(2):
                line = sys.stdin.readline()
                # Extract value from tab-separated input (last field)
                n = map(int, line.split('\t'))[-1]
                mul *= n  # Multiply the values
            
            # Add product to sum
            s += mul
        
        # Append computed cell value to current row
        r.append(s)
    
    # Append completed row to result matrix
    matrix.append(r)

# Print the result matrix (one row per line)
print('\n'.join([str(x) for x in matrix]))
