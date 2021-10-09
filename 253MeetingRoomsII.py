class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        min_heap = []
        intervals.sort(key=lambda x:x[0])
        for start, end in intervals:
            if len(min_heap) > 0 and min_heap[0] <= start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        return len(min_heap)