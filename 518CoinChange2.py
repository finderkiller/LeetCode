#Memo
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.table = {}
        return self.helper(amount, sorted(coins, reverse=True), 0)
    def helper(self, amount, coins, start):
        if amount == 0:
            return 1
        if amount < 0 or len(coins)==start:
            return 0
        if (amount, start) in self.table:
            return self.table[(amount, start)]
        ways = 0
        coin_amount = coins[start]
        remain_amount = amount
        while remain_amount >= 0:
            ways += self.helper(remain_amount, coins, start+1)
            remain_amount -= coin_amount
        self.table[(amount, start)] = ways
        return ways

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