class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x:x[0])
        min_heap = []
        for interval in intervals:
            if len(min_heap) != 0 and min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
        return len(min_heap)