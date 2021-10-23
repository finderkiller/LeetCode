#time: O(s), space: O(s)
"""
char odd count <= 2, k == 2
char odd count <= 3, k == 3
char odd count <= 4, k == 4

"""

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        count_table = {}
        for char in s:
            if char not in count_table:
                count_table[char] = 0
            count_table[char] += 1
        odd_count = 0
        for count in count_table.values():
            if count %2 == 1:
                odd_count += 1
        return odd_count <= k