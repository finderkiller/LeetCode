class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.queue.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        idx = 0
        while idx < len(self.queue):
            if timestamp - self.queue[idx] >= 300:
                self.queue.pop(0)
                continue
            idx += 1
        return idx
        

#follow up
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if len(self.queue) == 0 or self.queue[-1][0] != timestamp:
            self.queue.append((timestamp, 1))
            return
        self.queue[-1] = (self.queue[-1][0], self.queue[-1][1]+1)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        idx = 0
        count = 0
        while idx < len(self.queue):
            if timestamp - self.queue[idx][0] >= 300:
                self.queue.pop(0)
                continue
            count += self.queue[idx][1]
            idx += 1
        return count