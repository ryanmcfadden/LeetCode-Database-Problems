# LeetCode: https://leetcode.com/problems/nth-highest-salary/

# Difficulty: Medium
import pandas as pd

# Option 1: Not resting indices
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    salary = employee["salary"].drop_duplicates().sort_values(ascending=False)

    if len(salary) < N or N < 1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})": [salary.iloc[N-1]]})

# Option 2: Resting indices
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    salary = employee["salary"].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    if len(salary) < N or N < 1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})": [salary.loc[N-1]]})
