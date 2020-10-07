class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.helper(coins, 0, 0, amount)
    
    def helper(self, coins, start, current, target):
        if current == target:
            return 1
        if current > target:
            return 0
        result = 0
        for idx in range(start, len(coins)):
            result += self.helper(coins, idx, current+coins[idx], target)
        return result
#Memo
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.table = {}
        return self.helper(coins, 0, 0, amount)
    
    def helper(self, coins, start, current, target):
        if current == target:
            return 1
        if current > target:
            return 0
        if (start, current) in self.table:
            return self.table[(start, current)]
        result = 0
        for idx in range(start, len(coins)):
            result += self.helper(coins, idx, current+coins[idx], target)
        self.table[(start, current)] = result
        return result
#DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount < 0:
            return 0
        table = [0 for i in range(amount+1)]
        table[0]=1
        for coin in coins:
            for idx in range(coin, len(table)):
                table[idx] += table[idx-coin]
        return table[-1]