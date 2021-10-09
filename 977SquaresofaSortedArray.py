#O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        pivot = 0
        res = []
        for idx in range(len(nums)):
            if nums[idx] < 0:
                pivot += 1
            else:
                break
        right = pivot
        left = pivot - 1
        while left >= 0 or right < len(nums):
            if left < 0:
                res.append(nums[right]**2)
                right += 1
            elif right == len(nums):
                res.append(nums[left]**2)
                left -= 1
            elif nums[right] < abs(nums[left]):
                res.append(nums[right]**2)
                right += 1
            elif nums[right] >= abs(nums[left]):
                res.append(nums[left]**2)
                left -= 1
        return res