#!/usr/bin/env python
"""
DGIM Algorithm Implementation (Datar-Gionis-Indyk-Motwani)

Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
Course: Big Data Analytics & Computational Lab -I (BDA&CL-I)
Experiment 8: Implementation of DGIM Algorithm
Date: October 5, 2021
Repository: https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I

Description:
The DGIM algorithm is an efficient algorithm for processing large binary streams.
It estimates the number of 1-bits in a sliding window over a binary stream using
limited memory. The algorithm maintains buckets to track positions of 1s, allowing
approximate counting with minimal space complexity.

Key Features:
- Space-efficient: O(log²N) space complexity
- Sliding window support for stream processing
- Bucket-based representation of 1-bits
- Error bound: At most 50% error in count estimation

Algorithm Overview:
1. Maintains buckets of sizes that are powers of 2
2. Each bucket represents consecutive 1s with a timestamp
3. Merges buckets when more than 2 buckets of same size exist
4. Estimates count by summing bucket sizes within window
"""

# Input: Binary stream as space-separated bits
inp = list(map(int, input("Enter Elements : ").split()))

# Data structures
bucket_list = []          # List of buckets (start_index, end_index, size)
bucket_size_count = {}    # Dictionary to count buckets of each size

def checker():
    """
    Check and merge buckets to maintain DGIM invariant.
    Ensures at most 2 buckets of each size exist.
    """
    for ct in bucket_size_count.keys():
        # If more than 2 buckets of size ct exist
        if(bucket_size_count[ct] > 2):
            # Pop the two oldest buckets
            s2, e2, size2 = bucket_list.pop(-2)
            s1, e1, size1 = bucket_list.pop(-2)
            
            # Merge into a new bucket of double size
            bucket_list.insert(-1, (s1, e2, size1*2))
            
            # Update bucket size counts
            bucket_size_count[ct] -= 2
        else:
            # Update count for merged bucket size
            bucket_size_count[ct] = 1
            checker()  # Recursive check for new merged bucket

# Initialize indices and pair counter
start_index = 0
end_index = 0
pair = 0

# Process the binary stream
for i in range(len(inp)):
    bit = inp[i]
    
    # Process only 1-bits
    if(bit == 1):
        # Check if this bit pairs with previous bit
        if(pair == 1):
            end_index = i
            pair = 0
            
            # Create bucket for this pair
            bucket_list.append((start_index, end_index, 2))
            
            # Update bucket size count
            if 2 in bucket_size_count:
                bucket_size_count[2] += 1
            else:
                bucket_size_count[2] = 1
            
            # Check and merge if needed
            checker()
        else:
            # Start a new potential pair
            start_index = i
            pair = 1

# Display bucket information
print("Bucket Indexes Are : ", bucket_list)

# Extract bucket boundaries
starts = []
ends = []
for s, e, size in bucket_list:
    starts.append(s)
    ends.append(e)

# Display buckets as binary string
print("Buckets are ", end="")
for i in range(len(inp)):
    bit = inp[i]
    if(i in starts):
        print(" ", bit, end="")
    elif(i in ends):
        print(bit, end=" ")
    else:
        print(bit, end=" ")

# Get window size from user
k = int(input("\nEnter window size : "))
length = len(inp)

# Calculate window boundaries
bound1 = length - 1 - k
bound2 = length - 1

# Count 1s in the window using DGIM algorithm
ones_count = 0

for s, e, size in bucket_list[:-1]:
    # Check if bucket is within window
    if(s < bound1 and e < bound1):
        break  # Bucket is completely outside window
    elif(s <= bound1 and e >= bound1):
        # Bucket partially in window - count half
        ones_count += int(size/2)
    elif(s > bound1 and e >= bound1):
        # Bucket completely in window
        ones_count += size

# Display result
print(f"Number of 1s in Last {k} bits are", ones_count)

# Alternative implementation notes:
"""
For larger streams, consider:
1. Using timestamp-based bucket management
2. Implementing bucket expiration for old data
3. Optimizing bucket merging operations
4. Adding approximation error bounds calculation
"""
