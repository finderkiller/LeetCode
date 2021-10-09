#time: O(n*k), space: O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:
            return 0
        if k == 0:
            return 0
        result = 0
        right = 0
        left = 0
        table = {}
        while right < len(s):
            char = s[right]
            if char not in table:
                table[char] = 0
            table[char] += 1
            while len(table.keys()) > k:
                table[s[left]] = table[s[left]] - 1
                if table[s[left]] == 0:
                    table.pop(s[left])
                left += 1
            result = max(result, right-left+1)
            right += 1
        return result

#time: O(n), space: O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:
            return 0
        if k == 0:
            return 0
        left = 0
        right = 0
        result = 0
        table = {}
        while right < len(s):
            char = s[right]
            if char not in table:
                table[char] = 0
                k -= 1
            table[char] += 1
            while k < 0:
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    table.pop(s[left])
                    k += 1
                left += 1
            result = max(result, right-left+1)
            right += 1
        return result