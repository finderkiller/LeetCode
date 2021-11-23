#recursive, memo, time: s*n, space: s*n
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.table = {}
        result = self.helper(coins, 0, 0, amount)
        return result if result != sys.maxsize else -1
        
    def helper(self, coins, start, current, amount):
        if current == amount:
            return 0
        if current > amount:
            return -1
        if (start, current) in self.table:
            return self.table[(start, current)]
        result = sys.maxsize
        for idx in range(start, len(coins)):
            forward = self.helper(coins, idx, current+coins[idx], amount)
            if forward == -1:
                continue
            result = min(result, forward+1)
        self.table[(start, current)] = result
        return result
#DP, time: s*n, space = s
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [sys.maxsize for i in range(amount+1)]
        table[0] = 0
        for coin in coins:
            for idx in range(coin, len(table)):
                table[idx] = min(table[idx], table[idx-coin]+1)
        return table[-1] if table[-1] != sys.maxsize else -1