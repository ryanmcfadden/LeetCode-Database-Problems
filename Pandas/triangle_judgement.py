# LeetCode: https://leetcode.com/problems/triangle-judgement/description/

# Difficulty: Easy
import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    
  output = []

  for i in range(triangle.shape[0]):

    x, y, z = triangle.iloc[i]["x"], triangle.iloc[i]["y"], triangle.iloc[i]["z"]

    if (x+y>z) and (x+z>y) and (y+z>x):
      output.append("Yes")
    else:
      output.append("No")

  return pd.DataFrame({
    "x": triangle["x"],
    "y": triangle["y"],
    "z": triangle["z"],
    "triangle": output
  })
