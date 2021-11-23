#max_heap
#time: O(nlogn)
#space: O(n)
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        input = []
        for interval_list in schedule:
            for interval in interval_list:
                input.append(interval)
        input.sort(key = lambda x:x.start)
        import heapq
        max_heap = []
        result = []
        for interval in input:
            if len(max_heap) and -max_heap[0] < interval.start:
                result.append(Interval(-max_heap[0], interval.start))
            heapq.heappush(max_heap, -interval.end)
        return result