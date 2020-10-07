class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        low_capacity = 0
        high_capacity = sum(weights)
        for weight in weights:
            low_capacity = max(low_capacity, weight)

        while low_capacity < high_capacity:
            mid_capacity = low_capacity + (high_capacity - low_capacity)//2
            day = self.calcDays(weights, mid_capacity)
            if day < D:
                high_capacity = mid_capacity
            elif day == D:
                high_capacity = mid_capacity
            else:
                low_capacity = mid_capacity+1
        return low_capacity
    def calcDays(self, weights, capacity):
        count = 1
        cur_sum = 0
        for weight in weights:
            if cur_sum + weight <= capacity:
                cur_sum += weight
            else:
                cur_sum = weight
                count += 1
        return count