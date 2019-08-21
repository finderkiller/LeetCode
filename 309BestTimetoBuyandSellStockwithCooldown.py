class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sold = 0
        hold = -sys.maxsize-1
        rest = 0
        for price in prices:
            prev_sold = sold
            sold = hold+price
            hold = max(hold, rest-price)
            rest = max(rest, prev_sold)
        return max(rest, sold)
        
        