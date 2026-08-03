from typing import List

def maxProfit(prices: List[int]) -> int:
    Profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            Profit += prices[i] - prices[i - 1]
    return Profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  