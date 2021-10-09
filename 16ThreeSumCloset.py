class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return
        nums = sorted(nums)
        min_diff = sys.maxsize
        result = 0
        for idx in range(len(nums)-2):
            left = idx + 1
            right = len(nums)-1
            while left < right:
                total = nums[left] + nums[right] + nums[idx]
                if  total == target:
                    return nums[left] + nums[right] + nums[idx]
                if abs(total - target) < min_diff:
                    min_diff = abs(total - target)
                    result = total
                if nums[left] + nums[right] < target - nums[idx]:
                    left += 1
                elif nums[left] + nums[right] > target - nums[idx]:
                    right -= 1
        return result