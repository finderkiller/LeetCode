#time: O(n^2), O(n)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        table = [1 for i in range(len(arr))]
        
        max_length = 0
        for idx in range(len(table)):
            value = arr[idx]
            for num_idx in range(0, idx):
                if value - arr[num_idx] == difference:
                    table[idx] = max(table[idx], table[num_idx]+1)
            max_length = max(max_length, table[idx])
        return max_length

#time: O(n), space: O(n)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        table = {}
        max_length = 0
        for num in arr:
            table[num] = table.get(num-difference, 0) + 1
            max_length = max(max_length, table[num])
        return max_length