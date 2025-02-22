import numpy as np

# One player is the maker and the other is the taker.
# They agree on a width beforehand, such as 10.
# The taker generates a random integer between 1 and 100 inclusive (so each number has a 1% chance of appearing).
# This number is the true value of the contract. The taker sees the true value; the maker does not.

# There are ten rounds of action.
# In each round, the maker makes a market on the contract with the agreed upon width.
# For example, in the first round, the maker could say "45@55." The taker must trade one contract on this market.
# On the example market, the taker can buy for 55 ("take"), or sell at 45 ("sold").



class Market_Game:
    fair_values = np.arange(1, 101)
    widths = np.arange(0, 100, 2)
    
    def simulate_round(radius, fair_value, left, right):
        mid = left + (right - left) / 2
        if mid < fair_value: # Taker buys
            left = mid + 1
            return np.array([(mid + radius) - fair_value, -(mid + radius) + fair_value])
        else: # Taker sells
            right = mid - 1
            return np.array([-(mid - radius) + fair_value, (mid - radius) - fair_value])

                
        
        
    # Test cumulative expected value at 100 fair values for 50 market widths
    for width in widths:
        radius = width / 2
        total_PnL = np.array([0,0])
        for fair_value in fair_values:
            profits = np.array([0,0]) # [Maker, Taker]
            left = 1
            right = 100
            for i in range(10):
                profits = profits + simulate_round(radius, fair_value, left, right)
            total_PnL = total_PnL + profits
        print("Width: " + str(width) + " Total PnL: " + str(total_PnL))

# Using this simulation, we find that width = 50 give no edge to either player (for 10 rounds)

    