class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        while idx < len(intervals):
            interval = intervals[idx]
            if interval[1] < newInterval[0]:
                idx += 1
            elif interval[0] > newInterval[1]:
                intervals.insert(idx, newInterval)
                return intervals                
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                intervals.pop(idx)
        intervals.append(newInterval)
        return intervals