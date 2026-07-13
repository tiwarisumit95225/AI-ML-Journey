# 🐼 Pandas

## 📖 Overview

Pandas is a powerful Python library for data manipulation and analysis. It provides efficient data structures like **Series** and **DataFrame** that simplify working with structured datasets. Pandas is widely used in **Data Science**, **Machine Learning**, **Artificial Intelligence**, and **Data Analysis** for cleaning, transforming, analyzing, and preparing data.

---

# 📚 Topics Covered

## 1. Introduction to Pandas

- What is Pandas?
- Why use Pandas?
- Installing and importing Pandas
- Creating Series and DataFrames
- Understanding rows, columns, and indexes

---

## 2. DataFrame Basics

- Creating DataFrames from dictionaries
- Viewing DataFrames
- Shape, rows, and columns
- Column names and indexes
- `info()`
- `describe()`

---

## 3. Loading Data

- `read_csv()`
- `read_excel()`
- `read_json()`
- `read_parquet()`

---

## 4. Exploring Data

- `head()`
- `tail()`
- `sample()`
- `shape`
- `columns`
- `index`

---

## 5. Accessing Data

- `loc`
- `iloc`
- `at`
- `iat`
- Difference between `loc` and `iloc`

---

## 6. Sorting & Iterating

- `sort_values()`
- Ascending & Descending Sorting
- `iterrows()`

---

## 7. Filtering Data

- Single & Multiple Conditions
- Logical Operators (`&`, `|`, `~`)
- `isin()`
- `between()`
- `str.contains()`
- Regular Expressions (Regex)
- `query()`

---

## 8. DataFrame Column Operations

- Adding Columns
- Creating Columns from Existing Columns
- Mathematical Operations
- Conditional Columns
- Renaming Columns
- Removing Columns
- `inplace=True`

---

## 9. String & Datetime Operations

- String Methods (`.str`)
- `pd.to_datetime()`
- Working with Date & Time Columns

---

## 10. Saving Data

- `to_csv()`
- `to_excel()`
- `to_json()`
- `to_parquet()`

---

## 11. Handling Missing Values

- `isnull()`
- `isna()`
- `notna()`
- `dropna()`
- `fillna()`
- `interpolate()`

---

## 12. Merging & Concatenating

- `pd.merge()`
- Inner Join
- Left Join
- Right Join
- Outer Join
- `pd.concat()`

---

## 13. Advanced DataFrame Functions

- `apply()`
- Lambda Functions
- Custom Functions
- `map()`
- `replace()`
- `rename()`
- `astype()`
- Duplicate Handling
- `shift()`
- `rank()`
- `cumsum()`
- `rolling()`
- `reset_index()`

---

## 14. Aggregation & Analysis

- `sum()`
- `mean()`
- `median()`
- `min()`
- `max()`
- `count()`
- `std()`
- `describe()`
- `value_counts()`
- `groupby()`
- `agg()`
- `pivot_table()`

---

# 💻 Key Functions Learned

```python
import pandas as pd

# Reading Data
pd.read_csv()
pd.read_excel()
pd.read_json()
pd.read_parquet()

# Exploring Data
df.head()
df.tail()
df.sample()
df.info()
df.describe()

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

# 📂 Folder Structure

```text
Pandas/
│
├── data/
│
├── Mini_Projects/
│   └── Student-Performance-Analysis/
│
├── day1.ipynb
├── day2.ipynb
├── day3.ipynb
├── day4.ipynb
├── README.md
```

---

# 🚀 Mini Project Completed

## 📊 Student Performance Analysis

### Features

- Generated synthetic student dataset using Faker
- Data cleaning and preprocessing
- Feature engineering
- Grade and Result calculation
- Filtering students
- Sorting records
- GroupBy analysis
- Descriptive statistics
- Exporting analysis reports

### Concepts Applied

- Data Cleaning
- Feature Engineering
- Filtering
- Sorting
- GroupBy Analysis
- Aggregation
- Statistics
- CSV Export

---

# ✅ Status

- ✅ Introduction to Pandas
- ✅ DataFrame Basics
- ✅ Loading Data
- ✅ Exploring Data
- ✅ Accessing Data
- ✅ Sorting & Iterating
- ✅ Filtering Data
- ✅ Column Operations
- ✅ String & Datetime Operations
- ✅ Saving Data
- ✅ Handling Missing Values
- ✅ Merging & Concatenating
- ✅ Advanced DataFrame Functions
- ✅ Aggregation & Analysis
- ✅ Student Performance Analysis Project

## 🎉 Pandas Module Completed Successfully

---

# 🎯 Learning Outcomes

After completing this module, I can:

- Load and explore datasets
- Clean and preprocess data
- Handle missing values
- Create new features
- Filter and sort datasets
- Perform statistical analysis
- Use GroupBy and Aggregation
- Generate analysis reports
- Build complete Pandas-based data analysis projects

---

# 📌 Next Steps

- 📈 Matplotlib
- 🎨 Seaborn
- 📊 Data Visualization
- 🗄 SQL for Data Analysis
- 🤖 Machine Learning Data Preprocessing
- 📂 More Real-world Projects
- 🏆 Kaggle Practice