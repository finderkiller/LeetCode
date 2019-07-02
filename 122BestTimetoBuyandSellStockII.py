class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        total = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx-1]:
                total += prices[idx] - prices[idx-1]
        return total