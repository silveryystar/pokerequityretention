# Poker Equity Retention
A computational study of starting hand equity retention in Texas Hold 'em poker.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter `pip install numpy`.
5. Enter `pip install matplotlib`.
6. Enter `python main.py`.

# Methodology
Equities for all starting hands for 2- to 10-player Texas Hold 'em poker were gathered using Power-Equilab's Heatmap function (see http://power-equilab.com/).
Power-Equilab generates "equity matrices" via a 1000-second Monte Carlo simulation.
Results generated from Monte Carlo algorithms are generally accurate by the law of large numbers.
For the 2-player equity matrix, Power-Equilab utilized exhaustive enumeration.
The equity matrices generated through the heatmap function are located in folder *equity_matrices* in the repository.
A simplified plot containing all 9 equity matrices is located in folder *extra_plots*.

For each starting hand, its equity values per number of players were fitted to a power-law regression.
The power-law regression produces two variables, α and β, such that y=αx^β.
In this sense, α is normalized (0 player) equity, and β is equity retention.
In log-space, the power-law regression can be rewritten as log(y)=log(α)+βlog(x).
This process linearizes the equity function.

The constants in the linearized equity function, log(α) and β, are the main subjects analyzed in this study.
Plots of β versus log(α) and the patterns that emerge from various hand typologies are located in folder *β_log(α)_plots* in the repository.
Heatmaps of log(α) and β are located in folder *extra_plots*.
All values of log(α) and β derived in this study are located in *data.txt*.

# Results
This study concludes the following:
1. Pocket Aces have the highest equity retention among all hands.
2. Suited Connectors have the highest equity retention among non-big pocket pairs.
3. For any non-pocket pair hand, its suited variation has higher equity retention than its non-suited counterpart.
4. Equity retention and equity have no significant correlation.

Many Texas Hold 'em players will find conclusions 1 and 3 obvious.
On the other hand, conclusion 2 is a new discovery, with no clear proclamation in any literature.
Game Theory Optimal (GTO) ranges recommend playing most Suited Connectors in any position, supporting the high equity retention of Suited Connectors.

Conclusion 4 is also a new discovery.
Although a slight inverse proportionality exists between equity and equity retention, they are not significantly correlated.
This is important when translating equity between player changes, as a hand does not necessarily retain its equity despite its equity.
However, significant proportionality trends exist for specific hand typologies, as shown in the plots located in folder *β_log(α)_plots* in the repository.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.
