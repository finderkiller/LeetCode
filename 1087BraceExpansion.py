class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        input = []
        idx = 0 
        while idx < len(S):
            if S[idx] == "{":
                idj = idx+1
                tmp = ""
                while S[idj] != "}":
                    if S[idj] != ",":
                        tmp += S[idj]
                    idj += 1
                input.append("".join(sorted(tmp)))
                idx = idj
            else:
                input.append(S[idx])
            idx+=1
        collect = ""
        result = []
        self.helper(input, 0, collect, result)
        return result
    def helper(self, input, start, collect, result):
        if start == len(input):
            result.append(collect)
            return 
        for char in input[start]:
            self.helper(input, start+1, collect+char, result)