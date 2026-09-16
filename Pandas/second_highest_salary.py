# LeetCode: https://leetcode.com/problems/second-highest-salary/description/

# Difficulty: Medium
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
  salary = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
  if len(salary) < 2:
    second_salary = None
  else:
    second_salary = salary.iloc[1]

  return pd.DataFrame({"SecondHighestSalary": [second_salary]})
