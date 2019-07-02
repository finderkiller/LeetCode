class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        value = self.countAndSay(n-1)
        
        ret = ""
        idx = idj = 0
        while idx < len(value):
            count = 0
            while idj < len(value):
                if value[idx] == value[idj]:
                    count += 1
                    idj += 1
                else:
                    break
            ret += str(count) + value[idx]
            idx = idj
        return ret