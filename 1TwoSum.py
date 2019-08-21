class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return
        table = {}
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in table:
                return [table[remain], idx]
            table[num] = idx
        return []
            