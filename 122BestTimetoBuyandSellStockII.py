class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        total = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx-1]:
                total += prices[idx] - prices[idx-1]
        return total


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_price = prices[0]
        result = 0
        for idx in range(1, len(prices)):
            cur_price = prices[idx]
            if cur_price < buy_price:
                buy_price = cur_price
                continue
            result += cur_price - buy_price
            buy_price = cur_price
        return result