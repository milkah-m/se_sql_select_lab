# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
# Assign the variable `df_first_five` to the employee number and last name from all employees in the employees table 
# in the database. Your result should only contain those two columns.

df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)
print(df_first_five)

# STEP 3
# Repeat Step 2, but have the last name come before the employee number and assign to `df_five_reverse`.
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""", conn)
print(df_five_reverse)

# STEP 4
# Repeat step 3, but this time use an alias to rename the employee number column as 'ID' and assign to `df_alias`.
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber as 'ID'
FROM employees
""", conn)
print(df_alias)


# STEP 5
# Use `CASE` to bin where the jobTitles of President, VP Sales, or VP Marketing have the `role` of "Executive", 
# and the rest of the employes are "Not Executive".
# Define the result of the `CASE` as a new column called `role`. Assign to  the variable `df_executive`.
# ***Hint:*** For the WHEN clause if we were looking at Managers, we'd have:
# WHEN jobTitle = "Sales Manager (APAC)" OR jobTitle = "Sale Manager (EMEA)" OR jobTitle = "Sales Manager (NA)" THEN "Manager
df_executive = pd.read_sql("""
SELECT jobTitle,
CASE jobTitle
WHEN "President" THEN "Executive"
WHEN "VP Sales" THEN "Executive"
WHEN "VP Marketing" THEN "Executive"
ELSE "Not Executive"
END as role
FROM employees
""", conn)
print(df_executive)

# STEP 6
# Find the length of the last name for all employees, return only this data as a new column called `name_length`. 
# Assign to `df_name_length`.
df_name_length = pd.read_sql("""
SELECT length(lastName) as 'name_length'
FROM employees
""", conn)
print(df_name_length)

# STEP 7
# Return only one new column called `short_title`, that contains the first two letters of each persons job title. 
# Assign to `df_short_title`.
df_short_title = pd.read_sql("""
SELECT substr(jobTitle, 1,2) as 'short_title'
FROM employees
""", conn)
print(df_short_title)


order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Find the total amount for all orders, calculated as the sum of rounded total prices, where the total price for each order is the
# `priceEach` multiplied by the `quantityOrdered`. Make sure you are rounding this internal product result.
# Hint: Append `.sum()` to the end of your returned query that contains total price for each order, in order to create the total 
# amount. You could also use the `SUM()` built-in SQL function as well.

sum_total_price_df = pd.read_sql("""
SELECT SUM(round(priceEach * quantityOrdered)) as total
FROM orderDetails;
""", conn
)

sum_total_price = sum_total_price_df["total"]






# STEP 9
# It is common in other parts of the world as well as the US Military to have dates as Day/Month/Year. 
# Return the original order date column followed by three new columns that display the order date in this format with column names
#  'day', 'month', and 'year' respectively.
df_day_month_year = pd.read_sql("""
SELECT orderDate,
       strftime("%d", orderDate) AS day,
       strftime("%m", orderDate) AS month,
       strftime("%Y", orderDate) AS year
  FROM orders;
""", conn)

print(df_day_month_year)