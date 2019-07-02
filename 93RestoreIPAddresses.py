class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        prefix = []
        result = []
        self.helper(prefix, s, 4, result)
        return result
    def helper(self, prefix, s, level, result):
        if level == 0 and len(s) == 0:
            result.append(".".join(prefix))
            return
        elif level == 0 and len(s) > 0:
            return
        for idx in range(0, min(3, len(s))):
            value = s[:idx+1]
            if int(value) > 255:
                continue
            if len(value) > 1 and value[0] =="0":
                continue
            prefix.append(value)
            self.helper(prefix, s[idx+1:], level-1, result)
            prefix.pop()
            
        