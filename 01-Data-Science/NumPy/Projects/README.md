# Student Marks Analyzer using NumPy

## Overview

The **Student Marks Analyzer** is a beginner-friendly Python project built using the **NumPy** library. It analyzes student marks and generates useful statistics such as average marks, highest and lowest scores, grades, rankings, and pass percentage. This project was created to practice and demonstrate core NumPy concepts, including arrays, Boolean indexing, statistical functions, and sorting.

## Features

* Display student records
* Calculate total students and total marks
* Calculate average, highest, lowest, median, and standard deviation
* Display the class topper
* Display students scoring above 90 marks
* Display students scoring below the class average
* Generate grades (A, B, C, D, F)
* Display pass/fail status
* Rank students based on marks
* Display the top 3 students
* Show grade distribution
* Calculate pass percentage

## Technologies Used

* Python
* NumPy

## NumPy Concepts Used

* NumPy Arrays (`np.array()`)
* Statistical Functions

  * `np.sum()`
  * `np.mean()`
  * `np.max()`
  * `np.min()`
  * `np.median()`
  * `np.std()`
* Boolean Indexing
* Array Slicing (`[::-1]`)
* `np.argmax()`
* `np.argsort()`
* Boolean Masks
* Array Filtering

## Project Structure

```text
Student Marks Analyzer
│
├── student_marks_analyzer.py
└── README.md
```

## How to Run

1. Clone or download the project.
2. Install NumPy if it is not already installed:

   ```bash
   pip install numpy
   ```
3. Open the project in VS Code or any Python IDE.
4. Run the program:

   ```bash
   python student_marks_analyzer.py
   ```

## Sample Output

```text
==================================================
                 STATISTICS
==================================================

Total Students       : 6
Total Marks          : 505
Average Marks        : 84.17
Highest Marks        : 95
Lowest Marks         : 67
Median Marks         : 86.50
Standard Deviation   : 9.54
```

## Learning Outcomes

Through this project, I learned:

* Creating and working with NumPy arrays
* Performing statistical analysis using NumPy
* Using Boolean indexing for data filtering
* Finding maximum values and their indices
* Sorting arrays using `np.argsort()`
* Creating rankings from numerical data
* Formatting console output using Python f-strings
* Building a complete Python mini project with clean and organized code

## Future Improvements

* Read student data from a CSV file
* Support multiple subjects
* Add a search feature for students
* Visualize data using Matplotlib
* Analyze data using Pandas
* Build a graphical user interface (GUI)
* Export reports to a file

```
```
