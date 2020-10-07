class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        import heapq
        intervals = sorted(intervals, key=lambda x:x[0])
        min_heap = []
        for interval in intervals:
            if len(min_heap) == 0 or min_heap[0] > interval[0]:
                heapq.heappush(min_heap, interval[1])
                continue
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
            
        return len(min_heap)
        