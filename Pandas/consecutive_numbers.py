# LeetCode: https://leetcode.com/problems/consecutive-numbers/description/

# Difficulty: Medium
import pandas as pd

# Option 1: Using an array
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    
  num = logs["num"]
  cons_nums = []
    
  count=1
  for i in range(1,len(num)):      
    if num[i-1]==num[i]:  
      count+=1
    else:
      count=1

    if count >= 3 and num[i] not in cons_nums:
      cons_nums.append(num[i])

return pd.DataFrame({"ConsecutiveNums": cons_nums})

# Option 2: Using a set (feels more appropriate)
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    
    num = logs["num"]
    cons_nums = set()
    
    count=1
    for i in range(1,len(num)):
        
        if num[i-1]==num[i]:
            count+=1
        else:
            count=1

        if count >= 3:
            cons_nums.add(num[i])

    return pd.DataFrame({"ConsecutiveNums": list(cons_nums)})
