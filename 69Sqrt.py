# linear search, O(n)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        i = 1
        while i * i <= x:
            i+=1
        return i-1
# binary search, O(logn)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        return self.helper(1, x//2, x)
    def helper(self, start, end, target):
        if end < start:
            return end
        mid = start + (end-start)//2
        if mid * mid == target:
            return mid
        elif mid*mid < target:
            return self.helper(mid+1, end, target)
        else:
            return self.helper(start, mid-1, target)
