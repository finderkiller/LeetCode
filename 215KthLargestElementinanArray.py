#sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
#heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        if k > len(nums) or k < 0:
            return
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
# quick selection, Time complexity : O(N) in the average case, O(N^2)in the worst case.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        return self.helper(nums, 0, len(nums)-1, k)
        
    def helper(self, nums, start, end, k):
        if start == end:
            return nums[start]
        pivot_index = random.randint(start, end)
        self.swap(nums, end, pivot_index)
        pivot = nums[end]
        i = start-1
        for j in range(start, end):
            if nums[j] > pivot:
                i+=1
                self.swap(nums, i, j)
                
        i += 1
        self.swap(nums, i, end)
        if i == k-1:
            return nums[i]
        elif i > k-1:
            return self.helper(nums, start, i-1, k)
        else:
            return self.helper(nums, i+1, end, k)
    def swap(self, nums, pos1, pos2):
        if not nums:
            return
        tmp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tmp