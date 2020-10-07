class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums = sorted(nums)
        ret = []
        for idx in range(len(nums)):
            if idx != 0 and nums[idx] == nums[idx-1]:
                continue
            target = 0 - nums[idx]
            left = idx+1
            right = len(nums)-1
            while left < right:
                if left != idx+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right != len(nums)-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    ret.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return ret