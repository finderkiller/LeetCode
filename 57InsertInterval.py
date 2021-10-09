class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        inserted = False
        for idx in range(len(intervals)):
            start = intervals[idx][0]
            end = intervals[idx][1]
            if start >= newInterval[0]:
                inserted = True
                intervals.insert(idx, newInterval)
                break
        if not inserted:
            intervals.append(newInterval)
        result = [intervals[0]]
        for start, end in intervals[1:]:
            pre_start = result[-1][0]
            pre_end = result[-1][1]
            if start <= pre_end:
                result.pop()
                result.append([pre_start, max(pre_end, end)])
            else:
                result.append([start, end])
        return result