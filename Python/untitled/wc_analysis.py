import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

matches = pd.read_csv("WorldCups.csv",usecols=['MatchesPlayed'])
matches_played = np.array(matches)

goals = pd.read_csv("WorldCups.csv",usecols = ['GoalsScored'])
goal = np.array(goals)
np.sum(goal)
ortalama = np.sum(goal)/20 #ortalama gol sayısı
goal_avg = goal / matches_played #yıllara göre ortalama gol sayısı

print(goal_avg)


"""
(s[:,2] ==2).sum()
"""