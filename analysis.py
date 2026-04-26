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

#Now for a Scatter Plot of Win rate vs KDA
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

plt.scatter(vanguards_kda, vanguards_winrate, color="blue", label="Vanguard")
plt.scatter(duelists_kda, duelists_winrate, color="red", label="Duelist")
plt.scatter(strategists_kda, strategists_winrate, color="green",label="Strategist")

plt.legend()
plt.show()

#Here I'm gonna make a bar chart again but this time showing the heroes with the highest frequency of MVP/SVP
df["mvp_svp_rate"] = (df["MVPs"] + df["SVPs"]) / df["matches"]
#MVP Rate = # of MVP's + # of SVP's divided by # of matches

top_mvp_svp = df[df["matches"] >= 10].sort_values("mvp_svp_rate", ascending=True).tail(10)
#get top 10 highest MVP/SVP Rate

plt.barh(top_mvp_svp["hero"], top_mvp_svp["mvp_svp_rate"], color="gold", edgecolor="black")
plt.title("Top Heroes by MVP/SVP Frequency", fontweight="bold", color="Orange")
plt.xlabel("MVP or SVP Frequency")
plt.tight_layout()
plt.show()

#this part is for a pie chart to show the matches by role played. I am sure it will be overwhelmingly Vanguard though
roles = ["Vanguard","Duelist", "Strategist"]
matches = df.groupby("role")["matches"].sum()
colors = ["#EB3838", "#4CEB38", "#2754F5"]
roles_avg_winrate = df.groupby("role")["win_rate"].mean()

plt.title("Percentage of Time Played by Role", fontweight="bold", fontsize=20)
plt.pie(matches.values, labels = matches.index, autopct="%1.1f%%", colors = colors)
plt.show()