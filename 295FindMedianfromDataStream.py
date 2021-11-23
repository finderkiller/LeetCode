#time: O(1),
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.small_part = []
        self.large_part = []
        self.small_part_size = 0
        self.large_part_size = 0
        
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_part, -num)
        heapq.heappush(self.large_part, -heapq.heappop(self.small_part))
        self.large_part_size += 1
        if self.large_part_size > self.small_part_size:
            self.small_part_size += 1
            self.large_part_size -= 1
            heapq.heappush(self.small_part, -heapq.heappop(self.large_part))
       
    
    def findMedian(self) -> float:
        if not self.small_part and not self.large_part:
            return
        if self.small_part_size > self.large_part_size:
            return -self.small_part[0]
        return (self.large_part[0]-self.small_part[0])/2

#google questions, find median, mean and mode also by O(1)
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.small_part = []
        self.large_part = []
        self.small_part_size = 0
        self.large_part_size = 0
        self.count_table = {}
        self.most_count = 0
        self.mode = None
        self.total = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_part, -num)
        heapq.heappush(self.large_part, -heapq.heappop(self.small_part))
        self.large_part_size += 1
        if self.large_part_size > self.small_part_size:
            heapq.heappush(self.small_part, -heapq.heappop(self.large_part))
            self.large_part_size -= 1
            self.small_part_size += 1
        self.count_table[num] = self.count_table.get(num, 0) + 1
        if self.count_table[num] > self.most_count:
            self.most_count = self.count_table[num]
            self.mode = num
        self.total += num
        
    
    def findMedian(self) -> float:
        if self.small_part_size > self.large_part_size:
            return -self.small_part[0]
        return (self.large_part[0]-self.small_part[0])/2
        
        
    def findMean(self) ->float:
        return self.total/(self.small_part_size+self.large_part_size)
    
    def findMode(self) ->float:
        return self.mode