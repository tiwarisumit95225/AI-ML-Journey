# Matplotlib

## Overview

Matplotlib is one of the most popular Python libraries for data visualization. It is used to create static, animated, and interactive graphs that help in understanding and presenting data effectively. It is widely used in Data Science, Machine Learning, and Data Analysis.

---

# Why Matplotlib?

- Visualize data easily
- Identify trends and patterns
- Compare multiple datasets
- Present results clearly
- Create publication-quality graphs

---

# Topics Covered

## Introduction

- What is Data Visualization?
- What is Matplotlib?
- Importing Matplotlib

---

## Creating Figures

- `plt.figure()`
- Figure size (`figsize`)
- Resolution (`dpi`)

---

## Line Plots

- Creating a basic line graph
- Plotting multiple lines
- Labels using `label`

---

## Graph Customization

- Colors
- Line styles
- Line width
- Markers
- Marker size
- Marker edge color
- Shorthand format string (`fmt`)
- Font customization using `fontdict`

---

## Titles and Labels

- Graph title
- X-axis label
- Y-axis label
- Custom title formatting

---

## Axis Customization

- `plt.xticks()`
- `plt.yticks()`
- Custom tick intervals
- Displaying selected axis values

---

## Legend

- Adding legends using `plt.legend()`

---

## Bar Charts

- Creating bar charts using `plt.bar()`
- Customizing bar appearance
- Applying hatch (pattern) styles using `set_hatch()`
- Assigning hatch patterns dynamically using loops

---

## Saving and Displaying Graphs

- Saving graphs using `plt.savefig()`
- High-quality image export using `dpi`
- Displaying graphs using `plt.show()`

---

# Functions Learned

| Function | Description |
|----------|-------------|
| `plt.figure()` | Creates a new figure |
| `plt.plot()` | Creates a line plot |
| `plt.bar()` | Creates a bar chart |
| `plt.title()` | Adds a title |
| `plt.xlabel()` | Sets the X-axis label |
| `plt.ylabel()` | Sets the Y-axis label |
| `plt.xticks()` | Customizes X-axis ticks |
| `plt.yticks()` | Customizes Y-axis ticks |
| `plt.legend()` | Displays graph legend |
| `plt.savefig()` | Saves the graph as an image |
| `plt.show()` | Displays the graph |
| `BarContainer.set_hatch()` | Adds hatch patterns to bars |

---

# Mini Projects / Practice

### 📈 Gas Price Analysis

- Loaded CSV data using Pandas
- Compared gas prices of:
  - USA
  - Canada
  - South Korea
  - Australia
- Customized graph title, labels, legends, and X-axis ticks
- Exported the graph as a high-quality PNG (`dpi=300`)

### 📊 Bar Chart Customization

- Created a bar chart
- Applied hatch patterns (`/`, `o`, `*`)
- Used loops to assign patterns dynamically
- Learned how hatch improves graph readability

---

# Applications

- Data Analysis
- Machine Learning
- Deep Learning
- Scientific Computing
- Business Analytics
- Financial Analysis
- Research and Reporting

---

# Prerequisites

- Python
- NumPy (recommended)
- Basic Python programming knowledge

---

# Installation

```bash
pip install matplotlib
```

---

# Import

```python
import matplotlib.pyplot as plt
```

---

# Folder Structure

```
Matplotlib/
│
├── README.md
├── basics.ipynb
├── datasets/
├── images/
│   ├── basicgraph.png
│   └── gas_price_figure.png
```

---

# Learning Progress

- ✅ Introduction to Data Visualization
- ✅ Introduction to Matplotlib
- ✅ Creating Figures
- ✅ Figure Size & Resolution
- ✅ Basic Line Plots
- ✅ Multiple Line Plots
- ✅ Graph Customization
- ✅ Colors & Line Styles
- ✅ Markers
- ✅ Titles and Labels
- ✅ Font Customization
- ✅ Axis Ticks
- ✅ Legends
- ✅ Bar Charts
- ✅ Hatch Patterns
- ✅ Saving Figures

---

# Upcoming Topics

- Scatter Plots
- Histograms
- Pie Charts
- Subplots
- Grid
- Styles
- Figure and Axes Objects
- Legends (Advanced)
- Annotations
- Multiple Figures
- Real-world Data Visualization Projects

---

# Resources

- Official Documentation: https://matplotlib.org/
- Python Version: 3.x
- Library: Matplotlib

---

**Status:** 🟢 In Progress