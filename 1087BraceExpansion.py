class Solution:
    def expand(self, S: str) -> List[str]:
        if not S:
            return []
        collect = ""
        input = []
        result = []
        idx = 0
        while idx < len(S):
            if S[idx] == "{":
                idx += 1
                tmp = []
                while S[idx] != "}":
                    if S[idx] != ",":
                        tmp.append(S[idx])
                    idx += 1
                input.append("".join(sorted(tmp)))
            else:
                input.append(S[idx])
            idx += 1
        self.helper(collect, input, 0, result)
        return result
    
    def helper(self, collect, input, start, result):
        if start == len(input):
            result.append(collect)
            return
        for char in input[start]:
            self.helper(collect+char, input, start+1, result)