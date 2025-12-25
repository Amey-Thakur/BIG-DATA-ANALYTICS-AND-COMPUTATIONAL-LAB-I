#!/usr/bin/env python
"""
K-Means Clustering using PySpark and MapReduce

Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
Course: Big Data Analytics & Computational Lab -I (BDA&CL-I)
Experiment 9: Clustering Algorithm Using MapReduce
Date: October 5, 2021
Repository: https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I

Description:
This program implements K-Means clustering algorithm using PySpark's MLlib.
K-Means is an unsupervised learning technique that divides data points into K clusters
based on similarity. The algorithm uses MapReduce paradigm to process large datasets
efficiently in a distributed manner.

Dataset:
- CC_GENERAL.csv: Credit card customer data with 9K active cardholders
- Attributes: Balance, Purchases, Cash Advance, Credit Limit, Payments, etc.
- Goal: Customer segmentation for targeted marketing strategy

Algorithm Steps:
1. Load and inspect dataset schema
2. Feature engineering using VectorAssembler
3. Data standardization using StandardScaler
4. Apply K-Means clustering algorithm
5. Evaluate using Silhouette Score
6. Visualize clustering results

Requirements:
- Apache Spark with PySpark
- Python libraries: findspark, matplotlib
"""

# Import findspark to locate Spark installation
import findspark
findspark.init()

# Import PySpark modules
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Import visualization library
import matplotlib.pyplot as plt

# ========================================
# STEP 1: Create Spark Session
# ========================================
spark = SparkSession.builder \
    .appName("Clustering using K-Means") \
    .getOrCreate()

# ========================================
# STEP 2: Load Dataset
# ========================================
# Read CSV file with header and infer schema
data_customer = spark.read.csv(
    "CC_GENERAL.csv",
    header=True,
    inferSchema=True
)

# Display schema to understand data structure
print("Dataset Schema:")
data_customer.printSchema()

# ========================================
# STEP 3: Data Preprocessing
# ========================================
# Remove rows with null values
data_customer = data_customer.na.drop()

# Feature Selection: Select relevant columns for clustering
feature_columns = [
    'BALANCE',
    'BALANCE_FREQUENCY',
    'PURCHASES',
    'ONEOFF_PURCHASES',
    'INSTALLMENTS_PURCHASES',
    'CASH_ADVANCE',
    'PURCHASES_FREQUENCY',
    'ONEOFF_PURCHASES_FREQUENCY',
    'PURCHASES_INSTALLMENTS_FREQUENCY',
    'CASH_ADVANCE_FREQUENCY',
    'CASH_ADVANCE_TRX',
    'PURCHASES_TRX',
    'CREDIT_LIMIT',
    'PAYMENTS',
    'MINIMUM_PAYMENTS',
    'PRC_FULL_PAYMENT',
    'TENURE'
]

# ========================================
# STEP 4: Feature Engineering
# ========================================
# Convert multiple columns into a single feature vector
# VectorAssembler combines all features into a single vector column
assembler = VectorAssembler(
    inputCols=feature_columns,
    outputCol='features'
)

# Transform the dataset
assembled_data = assembler.transform(data_customer)

# Display transformed data (first 2 rows)
print("\nAssembled Features:")
assembled_data.select('CUST_ID', 'BALANCE', 'features').show(2)

# ========================================
# STEP 5: Feature Scaling
# ========================================
# Standardize features to bring them to a comparable scale
# This is important for distance-based algorithms like K-Means
scaler = StandardScaler(
    inputCol='features',
    outputCol='standardized',
    withStd=True,
    withMean=False
)

# Fit the scaler to the data and transform
data_scale = scaler.fit(assembled_data)
data_scale_output = data_scale.transform(assembled_data)

# Display standardized data
print("\nStandardized Features:")
data_scale_output.select('CUST_ID', 'BALANCE', 'standardized').show(2)

# ========================================
# STEP 6: K-Means Clustering
# ========================================
# Initialize K-Means clustering algorithm
# k: number of clusters to create
# featuresCol: column containing feature vectors
# predictionCol: output column for cluster assignments
# distanceMeasure: metric to calculate distance (Squared Euclidean)
kmeans_algo = KMeans(
    featuresCol='standardized',
    k=3  # Can be tuned based on silhouette score
)

# Train the K-Means model
kmeans_fit = kmeans_algo.fit(data_scale_output)

# Make predictions (assign clusters)
output = kmeans_fit.transform(data_scale_output)

# Display cluster assignments
print("\nCluster Assignments:")
output.select('CUST_ID', 'BALANCE', 'prediction').show(10)

# ========================================
# STEP 7: Model Evaluation
# ========================================
# Use Silhouette Score to evaluate clustering quality
# Silhouette Score ranges from -1 to 1
# Higher values indicate better-defined clusters
evaluator = ClusteringEvaluator(
    predictionCol='prediction',
    featuresCol='standardized',
    metricName='silhouette',
    distanceMeasure='squaredEuclidean'
)

# Calculate silhouette score for different k values
silhouette_scores = []
K_range = range(2, 10)

for k in K_range:
    kmeans = KMeans(featuresCol='standardized', k=k)
    model = kmeans.fit(data_scale_output)
    predictions = model.transform(data_scale_output)
    score = evaluator.evaluate(predictions)
    silhouette_scores.append(score)
    print(f"Silhouette Score for k={k}: {score}")

# ========================================
# STEP 8: Visualization
# ========================================
# Plot silhouette scores to find optimal k
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.plot(K_range, silhouette_scores, marker='o')
ax.set_xlabel('k')
ax.set_ylabel('Silhouette Score')
ax.set_title('Silhouette Score vs Number of Clusters')
plt.show()

# ========================================
# STEP 9: Stop Spark Session
# ========================================
spark.stop()

print("\nK-Means clustering completed successfully!")
print("Observations:")
print("- K-Means clustering partitions data into k clusters")
print("- Uses expectation-maximization technique")
print("- MapReduce enables distributed processing of large datasets")
print("- Silhouette score helps determine optimal number of clusters")
