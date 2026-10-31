# 📊 Pandas Analyzer & Data Visualization -- Python Project

**Author:** Jenisha Ramani

**Project Name:** Pandas Analyzer & Data Visualization

------------------------------------------------------------------------

## 📌 Project Overview

Pandas Analyzer & Data Visualization is a Python-based console
application developed using the Pandas, NumPy, Matplotlib and Seaborn
libraries. It provides sales data analysis and visualization through a
menu-driven program.

The project allows users to load a sales dataset in CSV format, explore
and clean the data, perform DataFrame operations, calculate statistics,
and create different types of plots and save them as image files.

It demonstrates the practical implementation of Pandas and
Object-Oriented Programming (OOP) concepts in Python through the
`SalesDataAnalyzer` class.

## 🛠️ Technology Used

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn
-   Visual Studio Code
-   GitHub

## ✨ Features

### 1. Load Dataset

-   Load a sales dataset from a CSV file.
-   Handle exceptions such as file not found.

### 2. Explore Data

-   Display the first and last 5 rows.
-   Display column names and data types.
-   Display basic information about the dataset.

### 3. Perform DataFrame Operations

-   NumPy array demo (indexing and slicing).
-   Mathematical operations (Profit and Discounted Sales).
-   Combine and split DataFrames.
-   Search, sort and filter data.
-   Aggregate functions (sum, mean, count).
-   Pivot tables.
-   Advanced operations using `groupby()` and `transform()`.

### 4. Handle Missing Data

-   Display rows with missing values.
-   Fill missing values with mean.
-   Drop rows with missing values.
-   Replace missing values with a specific value.

### 5. Generate Descriptive Statistics

-   describe()
-   Standard Deviation
-   Variance
-   Percentiles

### 6. Data Visualization

-   Bar Plot
-   Line Plot
-   Scatter Plot
-   Pie Chart
-   Histogram
-   Stack Plot

### 7. Save Visualization

-   Save the generated plot as an image file (PNG, JPEG).

## 📂 Project Structure

``` text
Pandas Analyzer & Data Visualization/
│
├── main.py
├── sales_data.csv
├── scatter_plot.png
├── output.png
└── README.md
```

## ▶️ How to Run the Project

### Step 1: Install the Required Libraries

``` bash
pip install pandas numpy matplotlib seaborn
```

### Step 2: Run the Python File

``` bash
python main.py
```

### Step 3: Load the Dataset

Choose option `1` first and enter `sales_data.csv`. All other options
work only after the dataset is loaded.

## 🗂️ Dataset Information

`sales_data.csv` contains 1000 sales records with the following columns:

`Product_ID`, `Sale_Date`, `Sales_Rep`, `Region`, `Sales_Amount`,
`Quantity_Sold`, `Product_Category`, `Unit_Cost`, `Unit_Price`,
`Customer_Type`, `Discount`, `Payment_Method`, `Sales_Channel`,
`Region_and_Sales_Rep`

Two extra columns, `Year` and `Month`, are created automatically from
`Sale_Date` while loading the data.

## 📝 Assumptions

-   Profit is calculated as `(Unit_Price - Unit_Cost) * Quantity_Sold`.
-   Discounted Sales is calculated as `Sales_Amount * (1 - Discount)`.
-   The dataset has no missing values; the missing-data options are still
    implemented for other datasets.
-   The stack plot uses Month and Region because almost all records
    belong to the year 2023.
-   Column names entered by the user must match the CSV exactly
    (case-sensitive).

## 💻 Sample Output

``` text
========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================

Enter your choice: 1

== Load Dataset ==
Enter the path of the dataset (CSV file): sales_data.csv
Dataset loaded successfully!

========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================

Enter your choice: 2

== Explore Data ==
1. Display the first 5 rows
2. Display the last 5 rows
3. Display column names
4. Display data types
5. Display basic info
Enter your choice: 1
   Product_ID  Sale_Date Sales_Rep Region  Sales_Amount  Quantity_Sold Product_Category  Unit_Cost  Unit_Price Customer_Type  Discount  \
0        1052 2023-02-03       Bob  North       5053.97             18        Furniture     152.75      267.22     Returning      0.09   
1        1093 2023-04-21       Bob   West       4384.02             17        Furniture    3816.39     4209.44     Returning      0.11   
2        1015 2023-09-21     David  South       4631.23             30             Food     261.56      371.40     Returning      0.20   
3        1072 2023-08-24       Bob  South       2167.94             39         Clothing    4330.03     4467.75           New      0.02   
4        1061 2023-03-24   Charlie   East       3750.20             13      Electronics     637.37      692.71           New      0.08   

  Payment_Method Sales_Channel Region_and_Sales_Rep  Year  Month  
0           Cash        Online            North-Bob  2023      2  
1           Cash        Retail             West-Bob  2023      4  
2  Bank Transfer        Retail          South-David  2023      9  
3    Credit Card        Retail            South-Bob  2023      8  
4    Credit Card        Online         East-Charlie  2023      3  

========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================

Enter your choice: 3

== DataFrame Operations ==
1. Numpy array demo (indexing/slicing)
2. Mathematical operations
3. Combine data
4. Split data
5. Search / Sort / Filter
6. Aggregate functions
7. Pivot table
8. Advanced (groupby + transform)
Enter your choice: 2
   Sales_Amount  Discount  Discounted_Sales   Profit
0       5053.97      0.09           4599.11  2060.46
1       4384.02      0.11           3901.78  6681.85
2       4631.23      0.20           3704.98  3295.20
3       2167.94      0.02           2124.58  5371.08
4       3750.20      0.08           3450.18   719.42

========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================

Enter your choice: 4

== Handle Missing Data ==
1. Display rows with missing values
2. Fill missing values with mean
3. Drop rows with missing values
4. Replace missing values with a specific value
Enter your choice: 1
No missing values found in the dataset!

========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================

Enter your choice: 5

== Descriptive Statistics ==
        Product_ID                   Sale_Date  Sales_Amount  Quantity_Sold    Unit_Cost   Unit_Price    Discount         Year       Month  \
count  1000.000000                        1000   1000.000000    1000.000000  1000.000000  1000.000000  1000.00000  1000.000000  1000.00000   
mean   1050.128000  2023-07-02 17:42:43.200000   5019.265230      25.355000  2475.304550  2728.440120     0.15239  2023.003000     6.50600   
min    1001.000000         2023-01-01 00:00:00    100.120000       1.000000    60.280000   167.120000     0.00000  2023.000000     1.00000   
25%    1024.000000         2023-03-30 00:00:00   2550.297500      13.000000  1238.380000  1509.085000     0.08000  2023.000000     3.00000   
50%    1051.000000         2023-06-30 12:00:00   5019.300000      25.000000  2467.235000  2696.400000     0.15000  2023.000000     6.00000   
75%    1075.000000         2023-10-12 00:00:00   7507.445000      38.000000  3702.865000  3957.970000     0.23000  2023.000000    10.00000   
max    1100.000000         2024-01-01 00:00:00   9989.040000      49.000000  4995.300000  5442.150000     0.30000  2024.000000    12.00000   
std      29.573505                         NaN   2846.790126      14.159006  1417.872546  1419.399839     0.08720     0.054717     3.54154   

             Profit  Discounted_Sales  
count   1000.000000       1000.000000  
mean    6487.847070       4248.637810  
min       17.360000         84.100000  
25%     1892.302500       2108.012500  
50%     5236.825000       4227.240000  
75%     9935.082500       6296.270000  
max    23441.110000       9715.870000  
std     5444.188837       2449.264594  

Std Dev  : 2846.79
Variance : 8104214.02
25th/50th/75th percentile: [2550.2975, 5019.3, 7507.445000000001]

========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================

Enter your choice: 6

== Data Visualization ==
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
Enter your choice: 3

== Scatter Plot ==
Enter x-axis column name: Quantity_Sold
Enter y-axis column name: Sales_Amount
Generating scatter plot...
Scatter plot displayed successfully!

========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================

Enter your choice: 7

== Save Visualization ==
Enter file name to save the plot (e.g., scatter_plot.png): scatter_plot.png
Visualization saved as scatter_plot.png successfully!

========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
===========================================================

Enter your choice: 8

Exiting the program. Goodbye!
```

## 📚 Learning Outcomes

Through this project, I learned:

-   Loading and exploring datasets using Pandas.
-   Handling missing data and cleaning datasets.
-   Performing mathematical operations on DataFrame columns.
-   Combining, splitting, searching, sorting and filtering data.
-   Using aggregate functions, pivot tables, `groupby()` and
    `transform()`.
-   Calculating statistical values such as standard deviation, variance
    and percentiles.
-   Creating Bar, Line, Scatter, Pie, Histogram and Stack plots using
    Matplotlib.
-   Saving visualizations as image files.
-   Implementing menu-driven applications in Python.
-   Applying Object-Oriented Programming concepts such as classes,
    constructor, destructor, inheritance and operator overloading.

