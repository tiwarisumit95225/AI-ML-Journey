# Pandas

## Overview

Pandas is a powerful Python library used for data manipulation and analysis. It provides efficient data structures like **Series** and **DataFrame** for handling structured data. It is widely used in Data Science, Machine Learning, Data Analysis, and AI for cleaning, transforming, analyzing, and preparing datasets.

---

# Topics Covered

### 1. Introduction to Pandas

* What is Pandas?
* Why use Pandas?
* Installing and importing Pandas
* Creating Series and DataFrames
* Understanding rows, columns, and indexes

### 2. DataFrame Basics

* Creating DataFrames from dictionaries
* Viewing DataFrames
* Understanding shape, rows, and columns
* Column names and indexes
* DataFrame information (`info()`)
* Statistical summary (`describe()`)

### 3. Loading Data

* Reading CSV files (`read_csv()`)
* Reading Excel files (`read_excel()`)
* Reading JSON files (`read_json()`)
* Reading Parquet files (`read_parquet()`)

### 4. Exploring Data

* `head()`
* `tail()`
* `sample()`
* `shape`
* `columns`
* `index`

### 5. Accessing Data

* Selecting single and multiple columns
* Accessing rows using `loc`
* Accessing rows using `iloc`
* Accessing single values using `at`
* Accessing single values using `iat`
* Difference between `loc` and `iloc`

### 6. Sorting & Iterating

* Sorting using `sort_values()`
* Ascending and descending order
* Iterating rows using `iterrows()`

### 7. Filtering Data

* Single and multiple conditions
* Logical operators (`&`, `|`, `~`)
* `isin()`
* `between()`
* String filtering using `str.contains()`
* Regular Expressions (Regex)
* Querying data using `query()`

### 8. DataFrame Column Operations

* Adding new columns
* Creating columns from existing columns
* Mathematical operations
* Conditional columns
* Renaming columns
* Removing columns (`drop()`, `del`)
* Using `inplace=True`

### 9. String & Datetime Operations

* String methods using `.str`
* Datetime conversion using `pd.to_datetime()`
* Working with date and time columns

### 10. Saving Data

* `to_csv()`
* `to_excel()`
* `to_json()`
* `to_parquet()`

### 11. Handling Missing Values

* `isnull()`
* `isna()`
* `notna()`
* `dropna()`
* `fillna()`
* `interpolate()`

### 12. Merging & Concatenating

* `pd.merge()`
* Merge types:

  * Inner Join
  * Left Join
  * Right Join
  * Outer Join
* `pd.concat()`
* Vertical (`axis=0`) and Horizontal (`axis=1`) concatenation

### 13. Advanced DataFrame Functions

* `apply()`
* Lambda functions
* Custom functions
* `map()`
* `replace()`
* `rename()`
* `astype()`
* Duplicate detection and removal
* `shift()`
* `rank()`
* `cumsum()`
* `rolling()`
* `reset_index()`

### 14. Aggregation & Analysis

* `sum()`
* `mean()`
* `median()`
* `min()`
* `max()`
* `count()`
* `std()`
* `describe()`
* `value_counts()`
* `groupby()`
* `agg()`
* Pivot Tables (`pivot_table()`)

---

# Key Functions Learned

```python
import pandas as pd

# Creating DataFrames
pd.DataFrame()

# Reading Files
pd.read_csv()
pd.read_excel()
pd.read_json()
pd.read_parquet()

# Exploring Data
df.head()
df.tail()
df.sample()

# Accessing Data
df.loc[]
df.iloc[]
df.at[]
df.iat[]

# Sorting
df.sort_values()

# Filtering
df.query()
df.isin()
df.between()
df["column"].str.contains()

# DataFrame Operations
df.drop()
df.rename()
df.apply()
df.map()
df.replace()
df.astype()

# Missing Values
df.isnull()
df.isna()
df.notna()
df.dropna()
df.fillna()
df.interpolate()

# Combining Data
pd.merge()
pd.concat()

# Saving Data
df.to_csv()
df.to_excel()
df.to_json()
df.to_parquet()

# Advanced Functions
df.shift()
df.rank()
df.cumsum()
df.rolling()
df.reset_index()

# Aggregation
df.groupby()
df.agg()
df.value_counts()
pd.pivot_table()
```

---

# Folder Structure

```text
Pandas/
│
├── day1.ipynb
├── day2.ipynb
├── day3.ipynb
├── day4.ipynb
├── README.md
└── data/
```

---

# Status

* ✅ Introduction to Pandas Completed
* ✅ DataFrame Basics Completed
* ✅ Loading Data Completed
* ✅ Exploring Data Completed
* ✅ Accessing Data Completed
* ✅ Sorting & Iterating Completed
* ✅ Filtering Data Completed
* ✅ Column Operations Completed
* ✅ String & Datetime Operations Completed
* ✅ Saving Data Completed
* ✅ Handling Missing Values Completed
* ✅ Merging & Concatenating Completed
* ✅ Advanced DataFrame Functions Completed
* ✅ Aggregation & Analysis Completed

**🎉 Pandas Learning Completed**

---

# Next Steps

* Mini Projects
* Real-world Dataset Analysis
* Kaggle Practice
* Matplotlib
* Seaborn
* Statistics
* Machine Learning Data Preprocessing
