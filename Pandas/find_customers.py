# LeetCode: https://leetcode.com/problems/customers-who-never-order/

# Difficulty: Easy
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
  customers_order = orders["customerId"]
    
  customers_no_order = customers[~customers["id"].isin(customers_order)]
    
  return pd.DataFrame({"Customers":customers_no_order["name"]})
