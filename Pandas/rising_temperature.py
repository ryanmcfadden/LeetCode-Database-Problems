# LeetCode: https://leetcode.com/problems/rising-temperature/

# Difficulty: Easy
import pandas as pd

# Option 1: Using a for loop
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    
  output_id = []
  weather = weather.sort_values(by="recordDate").reset_index(drop=True)

  for i in range(1,weather.shape[0]):

    if weather.iloc[i]["recordDate"] - weather.iloc[i-1]["recordDate"] == pd.Timedelta(days=1):
            
      if weather.iloc[i]["temperature"] > weather.iloc[i-1]["temperature"]:
        output_id.append(weather.iloc[i]["id"])

  return pd.DataFrame({"id":output_id})

# Option 2: Using shift commands
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
  weather = weather.sort_values("recordDate")

  previous_date = weather["recordDate"].shift(1)
  previous_temp = weather["temperature"].shift(1)

  result = weather[
    ((weather["recordDate"] - previous_date) == pd.Timedelta(days=1))
      & (weather["temperature"] > previous_temp)
  ]

  return result[["id"]]
