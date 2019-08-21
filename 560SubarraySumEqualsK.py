#Brute Force, O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        result = 0
        for idx in range(len(nums)):
            sum = nums[idx]
            if sum == k:
                result += 1
            for idj in range(idx+1, len(nums)):
                sum += nums[idj]
                if sum == k:
                    result += 1
        return result
#Hashtable, O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        table = {}
        sum = 0
        result = 0
        for idx in range(len(nums)):
            sum += nums[idx]
            if sum == k:
                result += 1
            result += table.get(sum-k, 0)
            table[sum] = table.get(sum, 0) + 1
        return result