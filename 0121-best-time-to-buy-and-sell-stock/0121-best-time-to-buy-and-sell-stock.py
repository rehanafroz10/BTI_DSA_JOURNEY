class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = float("inf")
        max_profit = 0

        for i in range(0, n):
            if prices[i] <= min_price:
                min_price = prices[i]
            else:
                p = prices[i] - min_price
                if p > max_profit:
                    max_profit = p

        return max_profit
