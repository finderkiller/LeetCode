# columnNumber -= 1 first, align with 0->A, 1->B,....,25->Z
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            mod = columnNumber%26
            result = chr(ord('A')+mod) + result
            columnNumber = columnNumber//26
        return result