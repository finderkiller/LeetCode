#time: O(n), space: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        return self.isPalindrome(s, 'left') or self.isPalindrome(s, 'right')
        
    def isPalindrome(self, s, skip_flag):
        left = 0
        right = len(s)-1
        one_skip = False
        while left <= right:
            if s[left] != s[right] and one_skip:
                return False
            elif s[left] != s[right]:
                one_skip = True
                if skip_flag == 'left':
                    left += 1
                elif skip_flag == 'right':
                    right -= 1
            else:
                left += 1
                right -= 1
        return True