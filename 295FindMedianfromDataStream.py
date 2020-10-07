class MedianFinder(object):
    import heapq
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_part = []
        self.large_part = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small_part, 0-num)
        heapq.heappush(self.large_part, 0-heapq.heappop(self.small_part))
        if len(self.large_part) > len(self.small_part):
            heapq.heappush(self.small_part, 0-heapq.heappop(self.large_part))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.small_part and not self.large_part:
            return
        if len(self.small_part) > len(self.large_part):
            return 0-self.small_part[0]
        return (self.large_part[0]-self.small_part[0])/2.0