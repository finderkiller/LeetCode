#sol1: using set
#sol2: sorting, O(nlogn), space: O(1), since in place modify
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx-1]:
                return nums[idx]

#sol3: binary search
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        return self.helper(nums, 1, len(nums)-1)
    
    def helper(self, nums, start_value, end_value):
        if start_value > end_value:
            return start_value
        mid_value = (start_value+end_value)//2
        
        count = 0
        for num in nums:
            if num <= mid_value:
                count += 1
        if count <= mid_value:
            return self.helper(nums, mid_value+1, end_value)
        else:
            return self.helper(nums, start_value, mid_value-1)
#sol4: tortoise and hare
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
#sol5: cyclic sort
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        for num in nums:
            next_idx = abs(num)
            if nums[next_idx] < 0:
                return abs(num)
            nums[next_idx] = -nums[next_idx]
            
        