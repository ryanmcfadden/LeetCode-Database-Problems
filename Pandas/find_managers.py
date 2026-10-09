# LeetCode: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

# Difficulty: Medium
import pandas as pd

# Option 1
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
  counts = employee["managerId"].value_counts()
  output = []

  for i in range(len(counts)): 
        
    if counts.iloc[i] >= 5:

      manager_index = counts.index[i]

      manager_name = employee.loc[employee["id"]==manager_index]["name"]

      output.extend(manager_name.tolist())  

  return pd.DataFrame({"name":output})

# Option 2
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    counts = employee["managerId"].value_counts()

    managers_ids = counts[counts>=5].index

    return employee.loc[employee["id"].isin(managers_ids),["name"]]
