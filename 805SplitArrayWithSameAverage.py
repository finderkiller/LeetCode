#DP
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        total = sum(A)
        possible = False
        for a in range(1, length):
            if (total * a) % length == 0:
                possible = True
        if not possible:
            return False
        dp = [set() for i in range(length)]
        dp[0] = [0] 
        for num in A:
            for dp_idx in range(length-1, 0, -1):
                for value in dp[dp_idx-1]:
                    dp[dp_idx].add(num + value)
        for a in range(1, length):
            if (total * a) % length == 0 and total * a/length in dp[a]:
                return True
           
        return False

#like combination sum III, using recursive
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        total = sum(A)
        for a in range(1, length):
            if (total * a) % length != 0:
                continue
            sum_a = total * a/length
            if self.helper(A, 0, a, sum_a):
                return True
        return False
            
    def helper(self, A, start, k, cur_sum):
        if start == len(A):
            return False
        if cur_sum == 0 and k == 0:
            return True
        if cur_sum < 0 or k == 0:
            return False
        for idx in range(start, len(A)):
            if idx != start and A[idx] == A[idx-1]:
                continue
            if self.helper(A, idx+1, k-1, cur_sum-A[idx]):
                return True
        return False
# sorted first
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        total = sum(A)
        A.sort()
        for a in range(1, length):
            if (total * a) % length != 0:
                continue
            sum_a = total * a/length
            if self.helper(A, 0, a, sum_a):
                return True
        return False
            
    def helper(self, A, start, k, cur_sum):
        if start == len(A):
            return False
        if cur_sum == 0 and k == 0:
            return True
        if cur_sum < 0 or k == 0:
            return False
        if A[start] > cur_sum/k:
            return False
        for idx in range(start, len(A)):
            if idx != start and A[idx] == A[idx-1]:
                continue
            if self.helper(A, idx+1, k-1, cur_sum-A[idx]):
                return True
        return False
        