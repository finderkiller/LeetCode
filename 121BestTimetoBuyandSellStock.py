class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_price = prices[0]
        max_profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] < buy_price:
                buy_price = prices[idx]
                continue
            max_profit = max(max_profit, prices[idx] - buy_price)
        return max_profit
        