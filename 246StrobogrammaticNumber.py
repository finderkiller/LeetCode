class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        start = 0
        end = len(num)-1
        while start <= end:
            if start == end:
                if num[start] == '1' or num[end] == '8' or num[start] == '0':
                    return True
            if num[start] == '1' and num[end] == '1':
                start += 1
                end -= 1
                continue
            if num[start] == '0' and num[end] == '0':
                start += 1
                end -= 1
                continue
            if num[start] == '6' and num[end] == '9':
                start += 1
                end -= 1
                continue
            if num[start] == '9' and num[end] == '6':
                start += 1
                end -= 1
                continue
            if num[start] == '8' and num[end] == '8':
                start += 1
                end -= 1
                continue
            else:
                return False
        return True