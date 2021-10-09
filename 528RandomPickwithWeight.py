class Solution:

    def __init__(self, w: List[int]):
        self.sum_weight = []
        for idx in range(len(w)):
            if idx == 0:
                self.sum_weight.append(w[0])
                continue
            self.sum_weight.append(w[idx]+self.sum_weight[idx-1])
        

    def pickIndex(self) -> int:
        import bisect
        import random
        number = random.randint(1, self.sum_weight[-1])
        insert_point = bisect.bisect_left(self.sum_weight, number)
        return insert_point


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()