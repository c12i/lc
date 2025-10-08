class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf')
        n = len(prices)
        
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit