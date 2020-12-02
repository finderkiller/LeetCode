class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[0])
        for idx in range(1, len(intervals)):
            start = intervals[idx][0]
            end = intervals[idx][1]
            if start < intervals[idx-1][1]:
                return False
        return True