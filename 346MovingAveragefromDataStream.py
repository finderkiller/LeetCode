class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.capacity = size
        self.size = 0
        self.array = []
        self.avg = 0
        

    def next(self, val: int) -> float:
        if self.capacity == 0:
            return 0
        if self.size == self.capacity:
            first_item = self.array[0]
            self.avg = (self.avg*self.size+val-first_item)/self.size
            self.array.pop(0)
            self.array.append(val)
            return self.avg
        else:
            total_sum = self.avg*self.size+val
            self.size += 1
            self.avg = total_sum/self.size
            self.array.append(val)
            return self.avg

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)