lass Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)
        while min_cap < max_cap:
            mid_cap = min_cap + (max_cap-min_cap)//2
            day = self.getDays(weights, mid_cap)
            if day <= D:
                max_cap = mid_cap
            else:
                min_cap = mid_cap+1
        return min_cap
        
    def getDays(self, weights, cap):
        day = 0
        cur_cap = 0
        for weight in weights:
            if cur_cap < weight:
                day += 1
                cur_cap = cap
            cur_cap -= weight
        return day
                