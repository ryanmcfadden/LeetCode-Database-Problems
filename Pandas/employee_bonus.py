# LeetCode: https://leetcode.com/problems/employee-bonus/

# Difficulty: Easy
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    
  employee = employee.merge(bonus, on="empId", how="left")

  employee = employee[(employee["bonus"] < 1000) | (employee["bonus"].isna())]

  return pd.DataFrame({
    "name": employee["name"],
    "bonus": employee["bonus"]
  })
