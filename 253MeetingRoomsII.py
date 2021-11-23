#time: O(nlogn),
#space: O(n)
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

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        import heapq
        min_heap = []
        total = 0
        max_room = 0
        for start, end in intervals:
            while len(min_heap) > 0 and min_heap[0] <= start:
                heapq.heappop(min_heap)
                total -= 1
            heapq.heappush(min_heap, end)
            total += 1
            max_room = max(max_room, total)
        return max_room