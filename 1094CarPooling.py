#heap, time: O(nlogn), space: O(n)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        min_heap = []
        total = 0
        import heapq
        for num_pass, start, end in trips:
            while len(min_heap) > 0 and min_heap[0][0] <= start:
                data = heapq.heappop(min_heap)
                total -= data[1]
            heapq.heappush(min_heap, (end, num_pass))
            total += num_pass
            if total > capacity:
                return False
        return True

#bucket sort, time: O(n), space: O(n)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        table = [0 for i in range(1001)]
        for num_pass, start, end in trips:
            table[start] += num_pass
            table[end] -= num_pass
         
        total = 0
        for value in table:
            total += value
            if total > capacity:
                return False
        return True