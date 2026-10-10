# LeetCode: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

# Difficulty: Easy
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
  result = orders["customer_number"].value_counts().index[0]

  return pd.DataFrame({"customer_number": [result]})
