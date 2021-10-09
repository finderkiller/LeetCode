"""
interval_result = []
1. traverse words, find in string
    if find: append (start and end) interval_result
2. merge interval
3. insert tag

time:O(m*n)
space:O(m) + O(n)
    

"""

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not words:
            return s
        if not s:
            return ""
        intervals = []
        merged_intervals = []
        result = ""
        for word in words:
            start_idx = s.find(word)
            while start_idx != -1:
                intervals.append([start_idx, start_idx+len(word)-1])
                start_idx = s.find(word, start_idx+1)
            
        if not intervals:
            return s
        intervals.sort(key=lambda x:x[0])
        merged_intervals.append(intervals[0])
        for idx in range(1, len(intervals)):
            start = intervals[idx][0]
            end = intervals[idx][1]
            if start <= merged_intervals[-1][1]+1:
                last_start, last_end = merged_intervals.pop()
                merged_intervals.append([last_start, max(end, last_end)])
            else:
                merged_intervals.append([start, end])
        
        idx = 0
        while idx < len(s):
            if not merged_intervals or idx != merged_intervals[0][0]:
                result += s[idx]
                idx += 1
                continue
            result += '<b>' + s[idx:merged_intervals[0][1]+1] + '</b>'
            idx += merged_intervals[0][1]-idx+1
            merged_intervals.pop(0)
        return result