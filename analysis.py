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


vanguards = df[(df["matches"]>=10.0) & (df["role"] == "Vanguard")]
vanguards_kda = vanguards["K/D/A"]
vanguards_winrate = vanguards["win_rate"]

duelists = df[(df["matches"]>=10.0) & (df["role"] == "Duelist")]
duelists_kda = duelists["K/D/A"]
duelists_winrate = duelists["win_rate"]

strategists = df[(df["matches"]>=10.0) & (df["role"] == "Strategist")]
strategists_kda = strategists["K/D/A"]
strategists_winrate = strategists["win_rate"]



plt.title("Win Rate by K/D/A", size=20, fontweight="bold", loc="left")
plt.xlabel("K/D/A", fontweight="bold")
plt.ylabel("Win Rate", fontweight="bold")

plt.scatter(vanguards_kda, vanguards_winrate, color="blue")
plt.scatter(duelists_kda, duelists_winrate, color="red")
plt.scatter(strategists_kda, strategists_winrate, color="green")
plt.show()