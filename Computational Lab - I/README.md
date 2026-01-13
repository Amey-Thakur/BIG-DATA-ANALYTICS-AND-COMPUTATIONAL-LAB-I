<!-- =========================================================================================
                                     HEADER SECTION
     ========================================================================================= -->
<div align="center">

  # Computational Lab - I

  ### CSL704 · Semester VII · Computer Engineering

  [![Curated by](https://img.shields.io/badge/Curated%20by-Amey%20Thakur-blue.svg)](https://github.com/Amey-Thakur)
  [![Documents](https://img.shields.io/badge/Documents-10-yellowgreen.svg)](#experiment-1-study-of-hadoop-system)
  [![Language](https://img.shields.io/badge/Language-Python%20%7C%20Cypher%20%7C%20MongoDB-orange.svg)](#experiment-1-study-of-hadoop-system)
  [![Type](https://img.shields.io/badge/Type-PDF%20%7C%20DOCX-blueviolet.svg)](#experiment-1-study-of-hadoop-system)

  **A comprehensive collection of laboratory experiments for Big Data Analytics focusing on Hadoop ecosystem, MapReduce programming, NoSQL databases, and data mining algorithms.**

  ---

  [How to Use](#how-to-use) &nbsp;·&nbsp; [Learning Path](#learning-path) &nbsp;·&nbsp; [Experiment 1](#experiment-1-study-of-hadoop-system) &nbsp;·&nbsp; [Experiment 2](#experiment-2-installation-of-hadoop) &nbsp;·&nbsp; [Experiment 3](#experiment-3-installation-and-configuration-of-sqoop) &nbsp;·&nbsp; [Experiment 4](#experiment-4-neo4j-graph-database-operations) &nbsp;·&nbsp; [Experiment 5](#experiment-5-matrix-multiplication-using-mapreduce) &nbsp;·&nbsp; [Experiment 6](#experiment-6-data-analysis-using-bigsheets) &nbsp;·&nbsp; [Experiment 7](#experiment-7-word-count-using-pyspark-mapreduce) &nbsp;·&nbsp; [Experiment 8](#experiment-8-dgim-algorithm-implementation) &nbsp;·&nbsp; [Experiment 9](#experiment-9-k-means-clustering-using-pyspark) &nbsp;·&nbsp; [Experiment 10](#experiment-10-mini-project)

</div>

---

> [!TIP]
> **Cluster Configuration**: For optimal learning, start with Hadoop Single-Node cluster setup (Experiments 1-2) before attempting Multi-Node configuration. Use Ubuntu/Linux virtual machines for better Hadoop compatibility. Keep separate development directories for MapReduce programs and dataset files to maintain clean project organization.

> [!WARNING]
> **Java Version Compatibility**: Hadoop 2.x requires Java 8 (NOT Java 11+). Using incompatible Java versions will cause ClassNotFoundException errors. Always verify `java -version` and `JAVA_HOME` settings before running MapReduce jobs. PySpark requires Python 3.6+ but may have compatibility issues with Python 3.10+ for certain libraries.

---

<!-- =========================================================================================
                                     HOW TO USE SECTION
     ========================================================================================= -->
## How to Use

### Running Hadoop Programs
1. **Configure** Hadoop single-node or multi-node cluster.
2. **Set** environment variables (JAVA_HOME, HADOOP_HOME).
3. **Execute** MapReduce jobs.

**Example:**
```bash
cd "Computational Lab - I/Experiment-5"
hadoop jar MatrixMultiplication.jar input output
```

### Running Neo4j Cypher Scripts
1. **Install** Neo4j Desktop or Server.
2. **Open** Neo4j Browser.
3. **Execute** Cypher queries.

**Example:**
```bash
cd "Computational Lab - I/Experiment-4"
# Copy queries from Neo4j_Car_Database.cypher and run in Neo4j Browser
```

### Running Python Scripts
**Environment Setup:**
Ensure **Python 3.x** is installed with required libraries (pandas, numpy, pyspark).

**Execution:**
```bash
cd "Computational Lab - I/Experiment-7"
spark-submit Word_Count_MapReduce.py
```

### Laboratory Reports
Each experiment includes comprehensive PDF reports covering:
- **Aim**: The specific Big Data objective.
- **Theory**: Theoretical background of the technology/algorithm.
- **Implementation**: Code explanation, architecture diagrams, and output screenshots.
- Use these reports as a reference for structuring your own lab submissions.

---

<!-- =========================================================================================
                                     LEARNING PATH SECTION
     ========================================================================================= -->
## Learning Path

### Phase 1: Hadoop Ecosystem
Understanding the foundation of distributed computing.
- **Experiment 1**: Study Hadoop architecture and components.
- **Experiment 2**: Install and configure Hadoop single-node cluster.
- **Experiment 3**: Integrate data using Sqoop for ETL operations.

### Phase 2: NoSQL & Graph Databases
Managing diverse data models.
- **Experiment 4**: Implement graph operations using Neo4j Cypher.
- **Experiment 6**: Analyze data using IBM BigSheets.

### Phase 3: MapReduce Programming
Parallel processing for large datasets.
- **Experiment 5**: Matrix multiplication using MapReduce.
- **Experiment 7**: Word count using PySpark MapReduce.

### Phase 4: Data Mining & Algorithms
Advanced analytics and data stream processing.
- **Experiment 8**: DGIM algorithm for data streams.
- **Experiment 9**: K-Means clustering with PySpark.
- **Experiment 10**: Stock Trading Strategy Optimization (Mini Project).

---

<!-- =========================================================================================
                                     EXPERIMENT 1
     ========================================================================================= -->
## Experiment 1: Study of Hadoop System

Study and analyze the Hadoop Ecosystem including HDFS architecture, MapReduce framework, and related components.

**Date:** July 20, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-1/AMEY_B-50_BDA_EXPERIMENT-1.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-1/AMEY_B-50_BDA_EXPERIMENT-1.docx) |
| — | Case Study (MD) | Hadoop in Banking - The Game Changer | [View](Experiment-1/Hadoop_Banking_Case_Study.md) |

---

<!-- =========================================================================================
                                     EXPERIMENT 2
     ========================================================================================= -->
## Experiment 2: Installation of Hadoop

Installation and configuration of Hadoop single-node cluster with verification of successful deployment.

**Date:** July 28, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-2/AMEY_B-50_BDA_EXPERIMENT-2.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-2/AMEY_B-50_BDA_EXPERIMENT-2.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 3
     ========================================================================================= -->
## Experiment 3: Installation and Configuration of Sqoop

Installation of Apache Sqoop for transferring bulk data between Hadoop and relational databases.

**Date:** September 09, 2021

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-3/AMEY_B-50_BDA_EXPERIMENT-3.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-3/AMEY_B-50_BDA_EXPERIMENT-3.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 4
     ========================================================================================= -->
## Experiment 4: Neo4j Graph Database Operations

Implementation of graph database operations using Neo4j Cypher query language for car database modeling.

**Date:** October 10, 2021

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Neo4j_Car_Database.cypher | Cypher queries for car database (nodes, relationships, queries) | [View](Experiment-4/Neo4j_Car_Database.cypher) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-4/AMEY_B-50_BDA_EXPERIMENT-4.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-4/AMEY_B-50_BDA_EXPERIMENT-4.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 5
     ========================================================================================= -->
## Experiment 5: Matrix Multiplication using MapReduce

Implementation of matrix multiplication using Hadoop MapReduce framework with Mapper and Reducer components.

**Date:** October 05, 2021

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Mapper.py | MapReduce Mapper for matrix multiplication | [View](Experiment-5/Mapper.py) |
| 2 | Reducer.py | MapReduce Reducer for matrix aggregation | [View](Experiment-5/Reducer.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-5/AMEY_B-50_BDA_EXPERIMENT-5.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-5/AMEY_B-50_BDA_EXPERIMENT-5.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 6
     ========================================================================================= -->
## Experiment 6: Data Analysis using Bigsheets

Data analysis and visualization using IBM BigSheets for processing and analyzing large datasets.

**Date:** October 05, 2021

| # | Resource | Description | Link |
|:-:|:---|:---|:-:|
| 1 | CeesVee.csv | Truck tracking dataset for BigSheets analysis | [View](Experiment-6/CeesVee.csv) |
| 2 | CSV_Head.csv | Field length data for analysis | [View](Experiment-6/CSV_Head.csv) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-6/AMEY_B-50_BDA_EXPERIMENT-6.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-6/AMEY_B-50_BDA_EXPERIMENT-6.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 7
     ========================================================================================= -->
## Experiment 7: Word Count using PySpark MapReduce

Implementation of word count algorithm using PySpark MapReduce for distributed text processing.

**Date:** October 05, 2021

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Word_Count_MapReduce.py | PySpark word count implementation | [View](Experiment-7/Word_Count_MapReduce.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-7/AMEY_B-50_BDA_EXPERIMENT-7.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-7/AMEY_B-50_BDA_EXPERIMENT-7.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 8
     ========================================================================================= -->
## Experiment 8: DGIM Algorithm Implementation

Implementation of DGIM (Datar-Gionis-Indyk-Motwani) algorithm for counting ones in a data stream.

**Date:** October 05, 2021

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | DGIM_Algorithm.py | DGIM algorithm for stream processing | [View](Experiment-8/DGIM_Algorithm.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-8/AMEY_B-50_BDA_EXPERIMENT-8.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-8/AMEY_B-50_BDA_EXPERIMENT-8.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 9
     ========================================================================================= -->
## Experiment 9: K-Means Clustering using PySpark

Implementation of K-Means clustering algorithm using PySpark for large-scale data clustering.

**Date:** October 05, 2021

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | KMeans_Clustering.py | PySpark K-Means clustering implementation | [View](Experiment-9/KMeans_Clustering.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-9/AMEY_B-50_BDA_EXPERIMENT-9.pdf) |
| — | Lab Report (DOCX) | Editable report file | [Download](Experiment-9/AMEY_B-50_BDA_EXPERIMENT-9.docx) |

---

<!-- =========================================================================================
                                     EXPERIMENT 10
     ========================================================================================= -->
## Experiment 10: Mini Project

<div align="center">

  ### 📈 [Optimizing Stock Trading Strategy with K-Means Clustering](https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I#big-data-analytics-mini-project)

  **Application of K-Means clustering algorithm to optimize stock trading strategies through pattern recognition in historical market data**

  [![Project](https://img.shields.io/badge/Project-Mini%20Project-purple.svg)](Experiment-10/BDA_MINI-PROJECT_REPORT_BE-COMPS_B-50%2C51%2C58.pdf)
  [![Platform](https://img.shields.io/badge/Platform-Hadoop%20%7C%20PySpark-yellowgreen.svg)](Experiment-10/BDA_MINI-PROJECT_REPORT_BE-COMPS_B-50%2C51%2C58.pdf)
  [![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)](Experiment-10/BDA_MINI-PROJECT_REPORT_BE-COMPS_B-50%2C51%2C58.pdf)

</div>

<div align="center">

  #### Authors
  | <img src="https://github.com/Amey-Thakur.png" width="150" alt="Amey Thakur"><br>[**Amey Thakur**](https://github.com/Amey-Thakur)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-A6CE39)](https://orcid.org/0000-0001-5644-1575) | <img src="../Mega/Mega.png" width="150" alt="Mega Satish"><br>[**Mega Satish**](https://github.com/msatmod)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--1844--9557-A6CE39)](https://orcid.org/0000-0002-1844-9557) | <img src="https://github.com/rizvihasan.png" width="150" alt="Hasan Rizvi"><br>[**Hasan Rizvi**](https://github.com/rizvihasan)<br><br>[![GitHub](https://img.shields.io/badge/GitHub-rizvihasan-181717?logo=github&logoColor=white)](https://github.com/rizvihasan) |
  | :---: | :---: | :---: |

</div>

> [!IMPORTANT]
> ### 🤝🏻 Special Acknowledgement
> *Special thanks to [**Mega Satish**](https://github.com/msatmod) and [**Hasan Rizvi**](https://github.com/rizvihasan) for their meaningful contributions, guidance, and support that helped shape this work.*

#### Project Overview

A Big Data analytics project that applies K-Means clustering to optimize stock trading strategies. The system analyzes historical stock market data to identify patterns and clusters that can inform trading decisions. By leveraging Big Data technologies like Hadoop and PySpark, the project demonstrates scalable processing of large financial datasets for pattern recognition and strategy optimization.

**Date:** October 22, 2021

#### Resources

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | Project Report | Comprehensive documentation and system design | [View](Experiment-10/BDA_MINI-PROJECT_REPORT_BE-COMPS_B-50%2C51%2C58.pdf) |
| 2 | Presentation | Visual overview of the development lifecycle | [View](Experiment-10/BDA_MINI-PROJECT_PPT_BE-COMPS_B-50%2C51%2C58.pdf) |

---

<!-- =========================================================================================
                                     FOOTER SECTION
     ========================================================================================= -->
<div align="center">

  <!-- Footer Navigation -->
  [↑ Back to Top](#computational-lab---i)

  [How to Use](#how-to-use) &nbsp;·&nbsp; [Learning Path](#learning-path) &nbsp;·&nbsp; [Experiment 1](#experiment-1-study-of-hadoop-system) &nbsp;·&nbsp; [Experiment 2](#experiment-2-installation-of-hadoop) &nbsp;·&nbsp; [Experiment 3](#experiment-3-installation-and-configuration-of-sqoop) &nbsp;·&nbsp; [Experiment 4](#experiment-4-neo4j-graph-database-operations) &nbsp;·&nbsp; [Experiment 5](#experiment-5-matrix-multiplication-using-mapreduce) &nbsp;·&nbsp; [Experiment 6](#experiment-6-data-analysis-using-bigsheets) &nbsp;·&nbsp; [Experiment 7](#experiment-7-word-count-using-pyspark-mapreduce) &nbsp;·&nbsp; [Experiment 8](#experiment-8-dgim-algorithm-implementation) &nbsp;·&nbsp; [Experiment 9](#experiment-9-k-means-clustering-using-pyspark) &nbsp;·&nbsp; [Experiment 10](#experiment-10-mini-project)

  <br>

  🏠 **[Back to Main Repository](../)** &nbsp;·&nbsp; 📈 **[Stock Trading Optimization with K-Means](https://github.com/Amey-Thakur/OPTIMIZING-STOCK-TRADING-STRATEGY-WITH-K-MEANS-CLUSTERING)**

</div>

---

<div align="center">

  ### [Big Data Analytics and Computational Lab I](https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I)

  **CSL704 · Semester VII · Computer Engineering**

  *University of Mumbai · Curated by [Amey Thakur](https://github.com/Amey-Thakur)*

</div>
