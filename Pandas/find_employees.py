# LeetCode: https://leetcode.com/problems/combine-two-tables/

# Difficulty: Easy
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    
  employee = employee.merge(employee, left_on="managerId", right_on="id")

  employee = employee[employee["salary_x"] > employee["salary_y"]]

  return pd.DataFrame({"Employee": employee["name_x"]})
