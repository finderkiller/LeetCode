#DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount == 0:
            return 0
        table = [sys.maxsize for i in range(amount+1)]
        table[0] = 0
        
        for idx in range(1, amount+1):
            for coin in coins:
                if idx-coin >= 0:
                    table[idx] = min(table[idx], table[idx-coin]+1)
        return table[amount] if table[amount] != sys.maxsize else -1

#DP coin放外層
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount == 0:
            return 0
        table = [sys.maxsize for i in range(amount+1)]
        table[0] = 0
        
        for coin in coins:
            for idx in range(1, amount+1):
                if idx-coin >= 0:
                    table[idx] = min(table[idx], table[idx-coin]+1)
        return table[amount] if table[amount] != sys.maxsize else -1