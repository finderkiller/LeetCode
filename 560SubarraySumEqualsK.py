#Brute Force, O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for start in range(len(nums)):
            cur_sum = 0
            for idx in range(start, len(nums)):
                cur_sum += nums[idx]
                if cur_sum == k:
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