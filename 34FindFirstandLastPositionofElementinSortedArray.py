class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) == 0:
            return [-1, -1]
        first = self.findFirst(nums, target)
        if first == -1:
            return [-1, -1]
        last = self.findLast(nums, target)
        return [first, last]
    
    def findFirst(self, nums, target):
        start = 0
        end = len(nums) -1
        while start <= end:
            mid = (end-start)//2 + start
            if nums[mid] == target:
                if mid-1 >= 0 and nums[mid-1] == target:
                    end = mid - 1
                else:
                    return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1
    def findLast(self, nums, target):
        start = 0
        end = len(nums) -1
        while start <= end:
            mid = (end-start)//2 + start
            if nums[mid] == target:
                if mid+1 <= len(nums)-1 and nums[mid+1] == target:
                    start = mid + 1
                else:
                    return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1