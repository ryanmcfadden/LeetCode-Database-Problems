# LeetCode: https://leetcode.com/problems/classes-with-at-least-5-students/

# Difficulty: Easy
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    
  class_count = courses["class"].value_counts()

  output = class_count[class_count >= 5].index

  return pd.DataFrame({"class":output})
