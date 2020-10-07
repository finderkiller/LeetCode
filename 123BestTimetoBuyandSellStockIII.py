class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_price = prices[0]
        leftProfit = [0 for i in range(len(prices))]
        left_max_profit = 0
        for idx in range(1, len(prices)):
            price = prices[idx]
            if price < buy_price:
                buy_price = price
            else:
                left_max_profit = max(left_max_profit, price-buy_price)
            leftProfit[idx] = left_max_profit
        
        right_max_profit = 0
        sell_price = prices[-1]
        total_max_profit = leftProfit[-1]
        for idx in range(len(prices)-2, -1, -1):
            price = prices[idx]
            if price > sell_price:
                sell_price = price
            else:
                right_max_profit = max(right_max_profit, sell_price-price)
            total_max_profit = max(total_max_profit, right_max_profit+leftProfit[idx])
        return total_max_profit