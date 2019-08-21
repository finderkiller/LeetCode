class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        prefix = ""
        table = {}
        table[2] = "abc"
        table[3] = "def"
        table[4] = "ghi"
        table[5] = "jkl"
        table[6] = "mno"
        table[7] = "pqrs"
        table[8]= "tuv"
        table[9] = "wxyz"
        self.helper(prefix, table, digits, 0, result)
        return result
    def helper(self, prefix, table, digits, start, result):
        if start == len(digits):
            result.append(prefix)
            return
        cur = int(digits[start])
        if cur not in table:
            return
        for char in table[cur]:
            self.helper(prefix+char, table, digits, start+1, result)