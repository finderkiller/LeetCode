"""
above two A, A->false
above LLL-> false
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = 0
        L_count = 0
        
        for idx, letter in enumerate(s):
            if letter == 'A':
                A_count += 1
            if letter == 'L':
                if L_count == 0:
                    L_count = 1
                elif idx > 0 and s[idx-1] == 'L':
                    L_count += 1
            else:
                L_count = 0
            if A_count == 2:
                return False
            if L_count == 3:
                return False
        return True

