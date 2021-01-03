class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx-1]:
                profit += prices[idx] - prices[idx-1]
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        buy_price = prices[0]
        for price in prices[1:]:
            if price <= buy_price:
                buy_price = price
            profit += price - buy_price
            buy_price = price
        return profit