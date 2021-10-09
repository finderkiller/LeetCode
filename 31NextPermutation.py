class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_small_idx = -1
        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] < nums[idx+1]:
                first_small_idx = idx
                break
        if first_small_idx == -1:
            nums.reverse()
            return
        
        first_larger_idx = -1
        for idx in range(len(nums)-1, -1, -1):
            if nums[idx] > nums[first_small_idx]:
                first_larger_idx = idx
                break
        tmp = nums[first_small_idx]
        nums[first_small_idx] = nums[first_larger_idx]
        nums[first_larger_idx] = tmp
        nums[first_small_idx+1:] = reversed(nums[first_small_idx+1:])