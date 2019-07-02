class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        return self.helper(nums, n, k-1)
    
    def helper(self, remain, n, k):
        if n == 1:
            return str(remain[0])
        index = k // self.factorial(n-1)
        value = remain[index]
        return str(value) + self.helper(remain[:index] + remain[index+1:], n-1, k%self.factorial(n-1))
    
    def factorial(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return n * self.factorial(n-1)