# LeetCode Database Solutions Using Pandas | Pandas Cheat Sheet

**Note:** This cheat sheet is a work in progress and will be regularly updated with new Pandas commands and explanations as I continue solving LeetCode Database problems.

This repository contains my solutions to LeetCode Database problems using the Pandas library in Python. It also includes a collection of commonly used Pandas commands that I've applied while solving these problems, along with explanations and examples. Think of it as a handy Pandas cheat sheet that you can refer to when practicing LeetCode problems, learning Pandas, or preparing for technical interviews.

For the examples in this cheat sheet, we'll assume that Pandas has already been imported using import pandas as pd and that a dataset has been loaded into a DataFrame named df (a commonly used variable name for Pandas DataFrames). We'll assume the DataFrame contains the following columns:
* 'Name' (string): The person's name.
* 'Age' (integer): The person's age.
* 'City' (string): The city where the person lives.
* 'Salary' (integer): The person's salary.
* 'Date' (string): A date stored as text.

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

**Note:** The key difference between .loc[] and .iloc[] is that .loc[] uses row and column labels, whereas .iloc[] uses integer positions. Similarly, .at[] and .iat[] are designed for accessing individual values using labels and positions, respectively.

## Cleaning and Modifying Data
* **Remove duplicate rows** from the entire DataFrame.
  + df.drop_duplicates()
* **Remove duplicate** values from the Salary column.
  + df["Salary"].drop_duplicates()
* **Remove duplicate rows based on the Salary column**, keeping the first occurrence.
  + df.drop_duplicates(subset=["Salary"])
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

## Merging Data Frames
Assume we have a second DataFrame named df2, which shares a common column, Name, with df. We can use pd.merge() to combine these DataFrames based on matching values in this column.

Merging DataFrames using different join types:
+ Inner Join (how="inner"): Returns only rows where Name exists in both df and df2.
  * pd.merge(df, df2, on="Name", how="inner")
+ Left Join (how="left"): Returns all rows from df, including matching data from df2. If no match is found, the corresponding values from df2 will be NaN.
  * pd.merge(df, df2, on="Name", how="left")
+ Right Join (how="right"): Returns all rows from df2, including matching data from df. If no match is found, the corresponding values from df will be NaN.
  * pd.merge(df, df2, on="Name", how="right")
+ Outer Join (how="outer"): Returns all rows from both df and df2, regardless of whether a match exists. Missing values are filled with NaN.
  * pd.merge(df, df2, on="Name", how="outer")

Note: The on="Name" parameter specifies the common column used to match records, while how determines which rows are included in the merged DataFrame. If duplicate names exist, a merge may produce multiple matching rows.  
