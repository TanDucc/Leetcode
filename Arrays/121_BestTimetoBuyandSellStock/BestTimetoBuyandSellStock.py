from typing import List

def maxProfit(self, prices: List[int]) -> int:
    left, right = 0, 1
    maxProfit = 0
    while right <len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1
    return maxProfit    

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(None, prices)) 