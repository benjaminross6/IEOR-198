import numpy as np

class Market_Game:
    fair_values = np.arange(1, 101)
    widths = np.arange(0, 100, 2)
    
    def sim_round(radius, fair_value, left, right):
        mid = left + (right - left) / 2
        if mid < fair_value: # Taker buys
            left = mid + 1
            return np.array([(mid + radius) - fair_value, -(mid + radius) + fair_value])
        else: # Taker sells
            right = mid - 1
            return np.array([-(mid - radius) + fair_value, (mid - radius) - fair_value])

                
        
    
    for width in widths:
        radius = width / 2
        total_PnL = np.array([0,0])
        for fair_value in fair_values:
            profits = np.array([0,0]) # [Maker, Taker]
            left = 1
            right = 100
            for i in range(10):
                profits = profits + sim_round(radius, fair_value, left, right)
            total_PnL = total_PnL + profits
        print("Width: " + str(width) + " Total PnL: " + str(total_PnL))


    