class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_profit = [0 for i in range(len(prices))]
        buy_price = prices[0]
        left_max_profit = 0
        for idx in range(1, len(prices)):
            price = prices[idx]
            if price < buy_price:
                buy_price = price
            left_max_profit = max(left_max_profit, price-buy_price)
            left_profit[idx] = left_max_profit
        right_max_profit = 0
        sell_price = prices[-1]
        result = 0
        
        for idx in range(len(prices)-2, -1, -1):
            price = prices[idx]
            if price > sell_price:
                sell_price = price
            right_max_profit = max(right_max_profit, sell_price-price)
            result = max(result, right_max_profit+left_profit[idx])
        return result