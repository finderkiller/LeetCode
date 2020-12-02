class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp < 0:
            return 0
        while self.queue and self.queue[0]+300 <= timestamp:
            self.queue.pop(0)
        return len(self.queue)
        

#follow up
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if len(self.queue) != 0 and self.queue[-1][0] == timestamp:
            self.queue[-1] = (timestamp, self.queue[-1][1]+1)
            return
        self.queue.append((timestamp, 1))
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp < 0:
            return 0
        while self.queue and self.queue[0][0]+300 <= timestamp:
            self.queue.pop(0)
        result = 0
        for time, count in self.queue:
            result += count
        return result