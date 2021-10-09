class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        array = s.split()
        for idx in range(len(array)):
            array[idx] = array[idx][::-1]
        return " ".join(array)