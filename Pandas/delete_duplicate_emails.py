# LeetCode: https://leetcode.com/problems/delete-duplicate-emails/

# Difficulty: Easy
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:

  # Failed certain test cases without including this line.
  person.sort_values(by="id", inplace=True)

  person.drop_duplicates(subset="email", keep="first", inplace = True)
