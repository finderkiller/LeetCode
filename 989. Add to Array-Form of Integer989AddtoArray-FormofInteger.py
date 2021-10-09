class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if not num:
            return [int(char) for char in str(k)]
        if not k:
            return num
        return [int(char) for char in str(int(''.join(map(str, num)))+k)]