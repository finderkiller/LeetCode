class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hasOneDuplicated = False
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i] and not hasOneDuplicated:
                hasOneDuplicated = True
                i +=1
                nums[i] = nums[j]
            elif nums[j] == nums[i] and hasOneDuplicated:
                continue
            elif nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                hasOneDuplicated = False
        return i+1