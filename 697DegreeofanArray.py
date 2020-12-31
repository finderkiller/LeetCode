class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        table = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1
        degree = max([value for key, value in table.items()])
        
        candidates = []
        for key, value in table.items():
            if value == degree:
                candidates.append(key)
        min_length = len(nums)
        for candidate in candidates:
            left = 0
            right = len(nums) - 1
            while left <= right:
                if nums[left] == candidate and nums[right] == candidate:
                    break
                if nums[left] != candidate:
                    left += 1
                if nums[right] != candidate:
                    right -= 1
            min_length = min(min_length, right-left+1)
        return min_length