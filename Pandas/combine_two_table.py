# LeetCode: https://leetcode.com/problems/combine-two-tables/

# Difficulty: Easy
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
  df = person.merge(address, on="personId", how="left")

  return df[["firstName","lastName","city","state"]]
