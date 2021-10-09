#time: O(n), space: O(n)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) <= 2:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)

#heap, time: O(n), space:O(1)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        import heapq
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > 3:
                heapq.heappop(min_heap)
        return min_heap[0] if len(min_heap) == 3 else max(nums)