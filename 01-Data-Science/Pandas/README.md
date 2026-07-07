# Pandas

## Overview

Pandas is a powerful Python library used for data manipulation and analysis. It provides efficient data structures like **Series** and **DataFrame** for handling structured data.

---

# Topics Covered

### 1. Introduction to Pandas

* What is Pandas?
* Why use Pandas?
* Installing and importing Pandas
* Creating a DataFrame
* Understanding rows, columns, and indexes

### 2. DataFrame Basics

* Creating DataFrames from dictionaries
* Viewing DataFrames
* Understanding shape, rows, and columns
* Column names and indexes

### 3. Loading DataFrames

* Reading CSV files using `read_csv()`
* Reading Excel files using `read_excel()`
* Reading JSON files using `read_json()`
* Reading Parquet files using `read_parquet()`
* Understanding different file formats

### 4. DataFrame Column Operations

* Adding new columns
* Creating columns from existing columns
* Modifying existing columns
* Removing columns using `drop()`
* Removing columns using `del`
* Using `inplace=True` for permanent changes

### 5. Accessing Data

* Selecting single and multiple columns
* Accessing rows using `loc`
* Accessing rows using `iloc`
* Accessing specific cell values
* Difference between `loc` and `iloc`

### 6. Filtering Data

* Filtering with single conditions
* Filtering with multiple conditions
* Using logical operators (`&`, `|`, `~`)
* Filtering with `isin()`
* Filtering with `between()`
* Filtering text using `str.contains()`

### 7. Handling Missing Values

* Detecting missing values with `isnull()` and `isna()`
* Counting missing values using `isnull().sum()`
* Removing missing values with `dropna()`
* Filling missing values using `fillna()`
* Understanding `NaN` values

### 8. Merging DataFrames

* Combining DataFrames using `pd.merge()`
* Merge types:

  * `inner`
  * `left`
  * `right`
  * `outer`
* Merging on common columns

### 9. Concatenating DataFrames

* Combining DataFrames using `pd.concat()`
* Vertical concatenation (`axis=0`)
* Horizontal concatenation (`axis=1`)
* Understanding index behavior during concatenation

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

# Accessing Data
df.loc[]
df.iloc[]

# DataFrame Operations
df.drop()
del df["column"]
df.apply()

# Filtering
df.isin()
df.between()
df["column"].str.contains()

# Missing Values
df.isnull()
df.isna()
df.notnull()
df.dropna()
df.fillna()

# Combining DataFrames
pd.merge()
pd.concat()
```

---

# Folder Structure

```text
Pandas/
│
├── day1.ipynb
├── day2.ipynb
├── README.md
└── data/
```

---

# Status

* ✅ Introduction to Pandas Completed
* ✅ DataFrame Basics Completed
* ✅ Loading DataFrames Completed
* ✅ DataFrame Column Operations Completed
* ✅ Accessing Data with `loc` and `iloc` Completed
* ✅ Filtering Data Completed
* ✅ Handling Missing Values Completed
* ✅ Merging DataFrames Completed
* ✅ Concatenating DataFrames Completed

---

# Next Topics

* Sorting Data
* Updating Values
* GroupBy Operations
* Aggregation Functions
* Joining DataFrames
* Pivot Tables
* Exporting Data
* Working with Dates and Time
* Duplicate Data Handling
* Apply, Map and Replace Functions
