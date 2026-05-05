# Marvel Rivals Personal Performance Analysis
Personal match data analysis using Python, pandas, and matplotlib

## Overview
I pulled together my data from tracker.gg to see my stats for all the heroes I've played and compiled that data into a csv file. I then used pandas and matplotlib to generate useful visualizations of that data like my K/D, win rate, MVPs/SVPs for each hero and role.

## Tools & Libraries

- Python 3
- pandas
- matplotlib

## Key Findings

#### Top Heroes by Win Rate
![Top Heroes by Win Rate](figures/Top_Heroes_by_Win_Rate.png)
- I'm truly surprised about the high win rate with Mantis but given only a little over 33 matches I've had as her, I would hesitate to truly count it. Wolverine is also a little surprising because I have no MVPs/SVPs as him but given that I have only 17 matches as him, I would expect the win rate to be a bit higher since I usually only go Wolverine when the enemy team is solo-tanking and that usually works out despite my mediocre Wolverine performance. Storm's 61% win rate is about what I would expect given the high MVP/SVP rate as well. Loki is the closest to the middle (50.9%) and above him is almost half the tank roster but I hesitate to really count Captain America since he has a lower number of matches. Just based off this chart, I would contemplate switching my "main" from Doctor Strange to either Mantis or Storm. Take note that almost all the Vanguards that I play, including my main, are near 50% win rate with Captain America being the highest (58.6%) and Emma Frost being the lowest (36%) which is rather surprising given that I mostly played Emma Frost when she had recently come out and had an incredibly strong diamond form. Then again, when I do tank, I am often solo tanking so that might be the reason as to why the win rates are so low compared to individual performance.

### MVP/SVP Frequency per Match
![MVP SVP Rate](figures/Top_Heroes_by_MVPSVP_Frequency.png)
- Here is the rate of how often I get MVP/SVP ((MVP+SVP)/#_of_matches), so this is a decent metric for individual performance. Here, Doctor Strange shows a strong lead with almost a 23% MVP/SVP followed by another Vanguard, Thor. Storm again shows up in the top 3 with a very strong 16.9% MVP/SVP rate. I would say this indicates strong performance as Storm correlates with a high win rate but I believe that a strong individual performance with high kills as Strange brings a lot less value, especially if solo-tanking. The last on this chart, Blade only has 1 MVP but is there because he has 10.2 matches so I would hesitate to count that one. 

### K/D/A vs. Win Rate by Role
![K/D vs Win Rate](figures/Win_Rate_by_KDA.png)
- Now that we've measured group performance and individual performance we can see if a strong individual performance actually means a higher win rate. Most characters are collected slightly lower-left of center. The far strategist outlier on the right is Ultron because of the high amount of assists he can get being a a more damage-centered strategist and Mantis is the higher win rate strategist outlier with an average K/D/A. Other than Mantis, the strategists I play show a decent trend to the right and upwards. The duelists show a weaker, steeper trend with Storm as somewhat of an outlier with a very high win rate and K/D/A. Vanguards on the other hand, do not show a strong trend in any direction and are more closely concentrated in the center.

## How to Run
1. Clone the repo
2. `pip install pandas matplotlib`
3. Open `notebook.ipynb` in Jupyter or run `analysis.py`
