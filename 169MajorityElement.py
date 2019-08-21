# sort
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return
        nums = sorted(nums)
        return nums[len(nums)//2]
        

# voting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return
        candidate = None
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
                count += 1
                continue
            count += 1 if candidate == value else -1
        return candidate
        