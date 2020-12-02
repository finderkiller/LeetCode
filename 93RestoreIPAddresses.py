class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        collect = []
        result = []
        self.helper(collect, s, 0, result)
        return result
        
    def helper(self, collect, string, start, result):
        if len(collect) == 4 and start == len(string):
            result.append(".".join(collect))
            return
        if len(collect) == 4:
            return
        tmp = ""
        for idx in range(start, min(start+3, len(string))):
            tmp += string[idx]
            if int(tmp) > 255:
                break
            if len (tmp) > 1 and tmp[0] == '0':
                break
            collect.append(tmp)
            self.helper(collect, string, idx+1, result)
            collect.pop()