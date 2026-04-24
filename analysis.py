import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/marvel_rivals_stats.csv")

top = df[(df["matches"] >= 10.0)].sort_values(by="win_rate", ascending=True).tail(20)
#this is making a data frame that only includes heroes with more than 10 matches, and then sorting them by win rate

plt.barh(top["hero"], top["win_rate"], color="green", edgecolor="black")

plt.title("Top Heroes by Win Rate", fontsize=15, fontfamily="Arial", color= "blue", fontweight="bold")
plt.xlabel("Win Rate", fontsize=17, fontfamily="Arial", color="red", fontweight="bold")
plt.ylabel("Hero", fontsize = 17, fontfamily="Arial", color="green", fontweight="bold")
plt.tight_layout()


plt.show()
