# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 00:23:01 2024

@author: Shefaa Ahmad Mestarihi
"""
import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/User/Downloads/Salaries.csv")

#Q1:

# 1. Number of Rows and Columns
num_rows, num_columns = df.shape
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")

# 2. Data Types of Each Column
data_types = df.dtypes
print("\nData Types of Each Column:")
print(data_types)

# 3. Check for Missing Values
missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

#Q2:
# 1. Calculate Mean, Median, Mode
mean_salary = df['TotalPay'].mean()
median_salary = df['TotalPay'].median()
mode_salary = df['TotalPay'].mode()[0]  # Mode may return multiple values, so we select the first one

# 2. Minimum and Maximum Salary
min_salary = df['TotalPay'].min()
max_salary = df['TotalPay'].max()

# 3. Calculate Range
salary_range = max_salary - min_salary

# 4. Calculate Standard Deviation
std_dev_salary = df['TotalPay'].std()

# Display the results
print(f"Mean Salary: {mean_salary}")
print(f"Median Salary: {median_salary}")
print(f"Mode Salary: {mode_salary}")
print(f"Minimum Salary: {min_salary}")
print(f"Maximum Salary: {max_salary}")
print(f"Salary Range: {salary_range}")
print(f"Standard Deviation of Salary: {std_dev_salary}")

#Q3:
# Replace missing values with the mean of the 'Benefits' column
df['Benefits'].fillna(df['Benefits'].mean, inplace=True)
#Method: Fill in missing values with a calculated or estimated value.
#Explanation: Imputation is useful when you want to retain as much data as possible. Common imputation techniques include replacing missing values with the mean, median, or mode of the respective column.
    
#Q4:
import matplotlib.pyplot as plt
import seaborn as sns
# 1. Histogram for Salary Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['TotalPay'], bins=20, kde=True, color='skyblue')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# 2. Pie Chart for Department Proportion
plt.figure(figsize=(8, 8))
department_counts = df['JobTitle'].value_counts()
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Proportion of Employees in Different Departments')
plt.show()

#Q5:
# Group by 'Department' and calculate summary statistics for each group
grouped_data = df.groupby('JobTitle')['TotalPay'].agg(['count', 'mean', 'median', 'min', 'max', 'std']).reset_index()

# Display the grouped data
print(grouped_data)

#Q6:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Calculate correlation
correlation = df['TotalPay'].corr(df['BasePay'])

# Plot scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='BasePay', y='TotalPay', data=df, color='skyblue')
plt.title(f'Scatter Plot: TotalPay vs {df["BasePay"].name} (Correlation: {correlation:.2f})')
plt.xlabel(df['BasePay'].name)
plt.ylabel('TotalPay')
plt.show()
