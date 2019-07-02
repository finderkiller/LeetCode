class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x:x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            cur_start = interval[0]
            cur_end = interval[1]
            last_start = result[len(result)-1][0]
            last_end = result[len(result)-1][1]
            
            if last_end >= cur_start:
                result[len(result)-1] = [last_start, max(cur_end, last_end)]
            else:
                result.append(interval)
        return result
        