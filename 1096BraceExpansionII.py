class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        if not expression:
            return []
        stk = []
        for char in expression:
            if char == "{":
                stk.append(char)
            elif char ==",":
                stk.append(char)
            elif char == "}":
                res = set()
                while stk and stk[-1] != "{":
                    if stk[-1] == ",":
                        stk.pop()
                        continue
                    res = res.union(stk.pop())
                stk.pop()
                
                if stk and stk[-1] != "{" and stk[-1] != ",":
                    tmp = set()
                    for s1 in stk.pop():
                        for s2 in res:
                            tmp.add(s1+s2)
                    res = tmp       
                stk.append(res)
            else:
                res = set()
                if stk and stk[-1] != "{" and stk[-1] != ",":
                    for s1 in stk.pop():
                        res.add(s1+char)
                else:
                    res.add(char)
                stk.append(res)
        return sorted(stk[0])