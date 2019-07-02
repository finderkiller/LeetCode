class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = 0 - sorted_nums[i]
            low = i+1
            high = len(sorted_nums)-1
            while low < high:
                if sorted_nums[low] + sorted_nums[high] == target:
                    result.append([sorted_nums[i], sorted_nums[low], sorted_nums[high]])
                    while low < high and sorted_nums[low] == sorted_nums[low+1]: #!記得是跟下一個比
                        low += 1
                    while low < high and sorted_nums[high] == sorted_nums[high-1]: #!記得是跟前一個比
                        high -= 1
                    low += 1
                    high -= 1
                elif (sorted_nums[low] + sorted_nums[high]) < target:
                    low += 1
                else:
                    high -= 1
        return result