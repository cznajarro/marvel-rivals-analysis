import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/marvel_rivals_stats.csv")

#this is just me making sure that matplotlib works and I can make a chart
top = df.sort_values(by="win_rate", ascending=False).head(15)

plt.title("Top Heroes by Win Rate", fontsize=15, fontfamily="Courier", color= "blue")
plt.barh(top["hero"], top["win_rate"], color="green")
plt.xlabel("Win Rate", fontsize=15, fontfamily="Courier", color="red")
plt.ylabel("Hero", fontsize = 15, fontfamily="Courier", color="green")
plt.tight_layout()
plt.show()
