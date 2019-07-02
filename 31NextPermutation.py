class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) == 0:
            return
        if len(nums) == 1:
            return
        smallFirst = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                smallFirst = i
                break
        if smallFirst == -1:
            nums.reverse()
            return
        largeFirst = -1
        for j in range(len(nums)-1, smallFirst, -1):
            if nums[j] > nums[smallFirst]:
                largeFirst = j
                break
        tmp = nums[smallFirst]
        nums[smallFirst] = nums[largeFirst]
        nums[largeFirst] = tmp
        self.reverse(nums, smallFirst+1, len(nums)-1)
        
        return
    def reverse(self, nums, i, j):
        while(i<j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
        return 