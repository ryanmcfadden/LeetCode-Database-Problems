# LeetCode: https://leetcode.com/problems/department-highest-salary/

# Difficulty: Medium
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
  employee = employee[employee.groupby("departmentId")["salary"].rank(method="dense", ascending=False) == 1]

  employee = employee.merge(department, left_on="departmentId", right_on="id")
    
  return pd.DataFrame({
    "Department": employee["name_y"],
    "Employee": employee["name_x"],
    "Salary": employee["salary"],
  })
