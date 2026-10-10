# LeetCode Database Solutions Using Pandas | Pandas Cheat Sheet

**Note:** This sheet is a work in progress and will be regularly updated with new Pandas commands and explanations as I continue solving LeetCode Database problems.

This repository contains my solutions to LeetCode Database problems using the Pandas library in Python. It also includes a collection of commonly used Pandas commands that I've applied while solving these problems, along with explanations and examples. Think of it as a handy Pandas cheat sheet that you can refer to when practicing LeetCode problems, learning Pandas, or preparing for technical interviews.

For the examples in this cheat sheet, we'll assume that Pandas has already been imported using import pandas as pd and that a dataset has been loaded into a DataFrame named df (a commonly used variable name for Pandas DataFrames). We'll assume the DataFrame contains the following columns:
* 'Name' (string): The person's name.
* 'Age' (integer): The person's age.
* 'City' (string): The city where the person lives.
* 'Salary' (integer): The person's salary.
* 'Date' (string): A date stored as text.

## Importing Data

## Exploring Data

## Selecting Data from a Data Frame
* Select a single column (Name) from the DataFrame.
  + df["Name"]
* Select multiple columns (Name and Age) from the DataFrame.
  + df[["Name", "Age"]]
* Select a specific row by its index label (row labelled 0).
  + df.loc[0]
* Select a specific value using row and column labels (the Name value at row label 0).
  + df.loc[0, "Name"]
* Select the first row by its position (regardless of its index label).
  + df.iloc[0]
* Select the first 3 rows by position (rows at positions 0, 1, and 2).
  + df.iloc[0:3]
* Select specific rows and columns by position (the first 3 rows and first 2 columns).
  + df.iloc[0:3, 0:2]
* Access a single value using row and column labels (the Age value at row label 0).
  + df.at[0, "Age"]
* Access a single value using row and column positions (the value in the first row and second column).
  + df.iat[0, 1]
* Select rows where values in the Salary column are not present in another DataFrame's Salary column.
  + df[~df["Salary"].isin(df2["Salary"])]
* Check whether values in the Salary column exist in a specified list.
  + df["Salary"].isin([40000, 50000])
* Exclude rows where the Salary column contains specified values.
  + df[~df["Salary"].isin([40000, 50000])]

**Note:** The key difference between .loc[] and .iloc[] is that .loc[] uses row and column labels, whereas .iloc[] uses integer positions. Similarly, .at[] and .iat[] are designed for accessing individual values using labels and positions, respectively.

## Comparing Consecutive Rows
* Shift values in the Salary column down by one row, allowing comparison with the previous value.
  + df["Salary"].shift(1)
* Identify rows where the Salary value matches the previous row.
  + df["Salary"] == df["Salary"].shift(1)
* Identify rows where the Salary value matches the previous two rows, indicating at least three consecutive identical values.
  + (df["Salary"] == df["Salary"].shift(1)) & (df["Salary"] == df["Salary"].shift(2))
* Identify where consecutive values change.
  + df["Salary"].ne(df["Salary"].shift())
* Assign a unique group number to each consecutive sequence of identical values.
  + df["Salary"].ne(df["Salary"].shift()).cumsum()

## Cleaning and Modifying Data
* **Remove duplicate rows** from the entire DataFrame.
  + df.drop_duplicates()
* **Remove duplicate** values from the Salary column.
  + df["Salary"].drop_duplicates()
* **Remove duplicate rows based on the Salary column**, keeping the first occurrence.
  + df.drop_duplicates(subset=["Salary"])
* **Remove duplicate rows based on the Salary column in place**, keeping the first occurrence.
  + df.drop_duplicates(subset="Salary", keep="first", inplace=True)
* **Rename a column** from Salary to Income.
  + df.rename(columns={"Salary": "Income"})
* **Remove the Salary column** from the DataFrame.
  + df.drop(columns=["Salary"])
* **Replace all occurrences** of London with LON throughout the DataFrame.
  + df.replace("London", "LON")
* **Add a new column named Bonus**, calculated as 50% of the Salary column.
  + df.assign(Bonus=df["Salary"] * 0.5)
* **Reset the DataFrame index to the default** sequential integers (0, 1, 2, ...) without retaining the old index.
  + df.reset_index(drop=True)
 
**Note:** Most of these operations return a new DataFrame without modifying the original df. To save the changes, assign the result back to df, for example:
  * df = df.drop_duplicates()
  * df = df.rename(columns={"Salary": "Income"})

## Sort Data
* **Sort rows by Salary in ascending order** (lowest to highest).
  + df.sort_values("Salary")
* **Sort rows by Salary in descending order** (highest to lowest).
  + df.sort_values("Salary", ascending=False)
* **Sort rows by their index** in ascending order.
  + df.sort_index()
* **Sort rows by their index** in descending order.
  + df.sort_index(ascending=False)
* **Retrieve the 3 rows** with the highest salaries.
  + df.nlargest(3, "Salary")
* **Retrieve the 3 rows** with the lowest salaries.
  + df.nsmallest(3, "Salary")
* **Sort rows by multiple columns**, first by Age in ascending order, then by Salary in descending order.
  + df.sort_values(by=["Age", "Salary"], ascending=[True, False])
* **Select specific columns** (Name and Salary) and sort the rows by Salary in descending order (highest to lowest).
  + df[["Name","Salary"]].sort_values(by="Salary", ascending=False)

**Note:** sort_values() and sort_index() return a new DataFrame by default without modifying the original. To save the sorted result, assign it back to df, for example: df = df.sort_values("Salary").

## Grouping and Aggregating Data
* **Group rows by Department**, allowing operations to be performed separately on each department.
  + df.groupby("Department")
* **Calculate multiple statistics** for the Salary column, such as the minimum and maximum salaries.
  + df["Salary"].agg(["min", "max"])
* **Count the number of employees in each city**, based on how frequently each value appears in the City column.
  + df["City"].value_counts()
* **Calculate the total salary for each department** by grouping employees by Department and summing their salaries.
  + df.groupby("Department")["Salary"].sum()
* **Calculate the average salary for each department**.
  + df.groupby("Department")["Salary"].mean()
* **Count the number of non-null salary values in each department**.
  + df.groupby("Department")["Salary"].count()
* **Calculate multiple statistics for each department**, such as the average and maximum salaries.
  + df.groupby("Department")["Salary"].agg(["mean", "max"])
* **Find the highest salary within each department**, returning the maximum salary for every employee in that department.
  + df.groupby("Department")["Salary"].transform("max")
* **Select employees earning the highest salary in their department**, including employees tied for the highest salary.
  + df[df["Salary"] == df.groupby("Department")["Salary"].transform("max")]
* **Rank salaries within each department in descending order**, assigning the same rank to equal salaries without skipping subsequent ranks.
  + df.groupby("Department")["Salary"].rank(method="dense", ascending=False)
* **Select the highest-paid employees in each department** using dense ranking.
  + df[df.groupby("Department")["Salary"].rank(method="dense", ascending=False) == 1]

**Note:** The key difference between .agg() and .transform() is that .agg() typically produces a summary for each group, whereas .transform() returns results aligned with the original rows. This makes .transform() particularly useful when filtering or comparing individual records against group-level statistics.

## Merging Data Frames
Assume we have a second DataFrame named df2, which shares a common column, Name, with df. We can use pd.merge() to combine these DataFrames based on matching values in this column.

Merging DataFrames using different join types:
* Inner Join (how="inner"): Returns only rows where Name exists in both df and df2.
  + pd.merge(df, df2, on="Name", how="inner")
* Left Join (how="left"): Returns all rows from df, including matching data from df2. If no match is found, the corresponding values from df2 will be NaN.
  + pd.merge(df, df2, on="Name", how="left")
* Right Join (how="right"): Returns all rows from df2, including matching data from df. If no match is found, the corresponding values from df will be NaN.
  + pd.merge(df, df2, on="Name", how="right")
* Outer Join (how="outer"): Returns all rows from both df and df2, regardless of whether a match exists. Missing values are filled with NaN.
  + pd.merge(df, df2, on="Name", how="outer")
* Merge two DataFrames using columns with different names, matching the Department column in df with the DepartmentID column in df2.
  + pd.merge(df, df2, left_on="Department", right_on="DepartmentID", how="inner")
* Perform a left join using differently named columns, keeping all rows from df and matching records from df2.
  + pd.merge(df, df2, left_on="Department", right_on="DepartmentID", how="left")
* Perform a right join using differently named columns, keeping all rows from df2 and matching records from df.
  + pd.merge(df, df2, left_on="Department", right_on="DepartmentID", how="right")
* Perform an outer join using differently named columns, keeping all rows from both DataFrames.
  +pd.merge(df, df2, left_on="Department", right_on="DepartmentID", how="outer")

**Note:** The on="Name" parameter specifies the common column used to match records, while how determines which rows are included in the merged DataFrame. If duplicate names exist, a merge may produce multiple matching rows. Use on="ColumnName" when both DataFrames share the same joining column name. Use left_on and right_on when the joining columns have different names.
