# LeetCode: https://leetcode.com/problems/game-play-analysis-i/

# Difficulty: Easy
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
  activity = activity.sort_values("event_date").drop_duplicates(subset="player_id", keep='first')

  return pd.DataFrame({
    "player_id": activity["player_id"],
    "first_login": activity["event_date"]
  })
