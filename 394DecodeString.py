class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        self.idx = 0
        return self.helper(s)
    def helper(self, s):
        result = ""
        while self.idx < len(s) and s[self.idx] != "]":
            if s[self.idx]<"0" or s[self.idx] >"9":
                result += s[self.idx]
                self.idx += 1
                continue
            freq = 0
            while s[self.idx] >= "0" and s[self.idx] <="9":
                freq = freq*10 + int(s[self.idx])
                self.idx += 1
            self.idx += 1
            string = self.helper(s)
            self.idx+=1
            for idx in range(freq):
                result += string
        return result
            
        