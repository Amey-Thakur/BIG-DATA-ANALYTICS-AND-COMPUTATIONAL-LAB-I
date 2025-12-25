#!/usr/bin/env python
"""
Word Count using PySpark and MapReduce

Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
Course: Big Data Analytics & Computational Lab -I (BDA&CL-I)
Experiment 7: Word Count Program using MapReduce
Date: October 5, 2021
Repository: https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I

Description:
This program implements a word count application using PySpark's MapReduce paradigm.
It reads text from an input file, tokenizes the words, performs mapping and reduction
operations, and outputs each unique word with its frequency count. The implementation
demonstrates the power of distributed computing for text processing tasks.

Requirements:
- Apache Spark
- PySpark (Python API for Spark)
- Python 3.x

Input:
- sample.txt: Text file containing the content to analyze

Output:
- Word frequency counts printed to console
"""

# Import required libraries
from pyspark import SparkConf, SparkContext

# Configure Spark application
# Set application name for identification in Spark UI
conf = SparkConf().setAppName("WordCount")

# Create Spark context with the configuration
sc = SparkContext(conf=conf)

# Read the input text file
# textFile() creates an RDD (Resilient Distributed Dataset) from the file
text_file = sc.textFile("file:///content/sample.txt")

# Perform MapReduce operations
# Step 1: flatMap() - Split each line into words
# Step 2: map() - Transform each word into a tuple (word, 1)
# Step 3: reduceByKey() - Aggregate counts for each word
counts = text_file.flatMap(lambda line: line.split()) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda x, y: x + y)

# Collect results from distributed RDD to driver program
# collect() brings all data back to a single machine
output = counts.collect()

# Print each word with its count
print("# Printing each word with its respective count")
for (word, count) in output:
    print("%s: %d" % (word, count))

# Stop the Spark context
# This releases resources and terminates the Spark session
sc.stop()

# Alternative approach using SparkSession (recommended for newer Spark versions)
"""
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \\
    .appName("WordCount") \\
    .getOrCreate()

# Read text file
text_file = spark.read.text("sample.txt")

# Perform word count using DataFrame API
from pyspark.sql.functions import explode, split

word_counts = text_file.select(explode(split(text_file.value, " ")).alias("word")) \\
    .groupBy("word") \\
    .count() \\
    .orderBy("count", ascending=False)

# Show results
word_counts.show()

# Stop Spark session
spark.stop()
"""
