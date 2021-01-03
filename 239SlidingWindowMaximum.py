#O(n*k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k > len(nums):
            return []
        result = []
        for idx in range(len(nums)-k+1):
            result.append(max(nums[idx:idx+k]))
        return result
#O(nlogk)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k > len(nums):
            return []
        import heapq
        heap = []
        result = []
        for idx in range(len(nums)):
            while heap and heap[0][1]<=idx-k:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[idx], idx))
            if idx+1 >= k:
                result.append(-heap[0][0])
        return result
#O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k > len(nums):
            return []
        deque = []
        result = []
        for idx in range(len(nums)):
            if deque and deque[0] <= idx-k:
                deque.pop(0)
            while deque and nums[deque[-1]]<nums[idx]:
                deque.pop()
            deque.append(idx)
            if idx+1 >= k:
                result.append(nums[deque[0]])
        return result