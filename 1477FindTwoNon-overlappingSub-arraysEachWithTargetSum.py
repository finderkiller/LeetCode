#sliding window + DP, always recording the min_length by end pointer, so it will cost another O(n) to find the min_pre_length before the start pointer

#time: O(n^2)
#space: O(n)
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        start = 0
        end = 0
        result = sys.maxsize
        min_table = {}
        cur_sum = 0
        while end < len(arr):
            cur_sum += arr[end]
            while start < end and cur_sum > target:
                cur_sum -= arr[start]
                start += 1
            if cur_sum == target:
                length = end-start+1
                min_pre_length = sys.maxsize
                for idx in range(start-1, -1, -1):
                    if idx not in min_table:
                        continue
                    min_pre_length = min(min_pre_length, min_table[idx])
                if min_pre_length != sys.maxsize:
                    result = min(result, length + min_pre_length)
                min_table[end] = length
            end += 1
        return result if result != sys.maxsize else -1

#sliding window + DP, always recording the min_length, index by index, if find target, just check the min_length from min_table[start-1]
# update the min_length index by index
#time: O(n)
#space: O(n)
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        start = 0
        end = 0
        result = sys.maxsize
        min_table = [sys.maxsize for i in range(len(arr))]
        cur_sum = 0
        while end < len(arr):
            cur_sum += arr[end]
            while start < end and cur_sum > target:
                cur_sum -= arr[start]
                start += 1
            if cur_sum == target:
                length = end-start+1
                if start > 0 and min_table[start-1] != sys.maxsize:
                    result = min(result, length + min_table[start-1])
                min_table[end] = min(min_table[end-1], length)
            else:
                min_table[end] = min_table[end-1]
            end += 1
        return result if result != sys.maxsize else -1