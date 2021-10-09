class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return[]
        #sorted
        intervals = sorted(intervals, key=lambda x:x[0])
        result = [intervals[0]]
        #traverse
        for idx in range(1, len(intervals)):
            new_start = intervals[idx][0]
            new_end = intervals[idx][1]
            #if overlap, merge
            if new_start >= result[-1][0] and new_start <= result[-1][1]:
                pre_interval = result.pop()
                result.append([pre_interval[0], max(new_end, pre_interval[1])])
            else:
                result.append(intervals[idx])
        return result
        