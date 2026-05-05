# Marvel Rivals Personal Performance Analysis
Personal match data analysis using Python, pandas, and matplotlib

## Overview
I pulled together my data from tracker.gg to see my stats for all the heroes I've played and compiled that data into a csv file. I then used pandas and matplotlib to generate useful visualizations of that data like my K/D, win rate, MVPs/SVPs for each hero and role.

## Tools & Libraries

- Python 3
- pandas
- matplotlib

### K/D vs. Win Rate by Role
![K/D vs Win Rate](figures/Win_Rate_by_KDA.png)

### MVP/SVP Frequency per Match
![MVP SVP Rate](figures/Top_Heroes_by_MVPSVP_Frequency.png)

## Key Findings

#### Top Heroes by Win Rate
![Top Heroes by Win Rate](figures/Top_Heroes_by_Win_Rate.png)
- I'm truly surprised about the high win rate with Mantis but given only a little over 33 matches I've had as her, I would hesitate to truly count it. Wolverine is also a little surprising because I have no MVPs/SVPs as him but given that I have only 17 matches as him, I would expect the win rate to be a bit higher since I usually only go Wolverine when the enemy team is solo-tanking and that usually works out despite my mediocre Wolverine performance. Storm's 61% win rate is about what I would expect given the high MVP/SVP rate as well. Loki is the closest to the middle (50.9%) and above him is almost half the tank roster but I hesitate to really count Captain America since he has a lower number of matches. Just based off this chart, I would contemplate switching my "main" from Doctor Strange to either Mantis or Storm. 

## How to Run
1. Clone the repo
2. `pip install pandas matplotlib`
3. Open `notebook.ipynb` in Jupyter or run `analysis.py`
