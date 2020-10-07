#recursive, memo, time: s*n, space: s*n
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        self.table = {}
        return self.helper(coins, 0, 0, amount)
    
    def helper(self, coins, start, current, amount):
        if current == amount:
            return 0
        if current > amount:
            return -1
        if (start, current) in self.table:
            return self.table[(start, current)]
        result = sys.maxsize
        for idx in range(start, len(coins)):
            ret = self.helper(coins, idx, current+coins[idx], amount)
            if ret == -1:
                continue
            result = min(result, 1+ret)
        self.table[(start, current)] = result if result != sys.maxsize else -1
        return self.table[(start, current)]
#DP, time: s*n, space = s
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [sys.maxsize for i in range(amount+1)]
        table[0] = 0
        
        for coin in coins:
            for value in range(coin, len(table)):
                table[value] = min(table[value], 1+table[value-coin])
        return table[-1] if table[-1] != sys.maxsize else -1