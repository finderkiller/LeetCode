class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        if len(nums) < 4:
            return result
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j]== nums[j-1]:
                    continue
                low = j+1
                high = len(nums)-1
                while low < high:
                    four_sum = nums[i] + nums[j] + nums[low] + nums[high]
                    if four_sum == target:
                        result.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif four_sum < target:
                        low += 1
                    else:
                        high -= 1
        return result
                