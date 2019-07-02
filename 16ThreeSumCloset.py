class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = nums[0]+nums[1]+nums[len(nums)-1]
        for idx in range(len(nums)-2):
            low = idx+1
            high = len(nums)-1
            while(low < high):
                threesum = nums[idx] + nums[low] + nums[high]
                if threesum < target:
                    low += 1
                else:
                    high -= 1
                if abs(target-threesum) < abs(target-result):
                    result = threesum
            
        return result
                
                
            
            