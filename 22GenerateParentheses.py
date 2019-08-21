class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        result = set()
        prev_list = self.generateParenthesis(n-1)
        for prev in prev_list:
            result.add("()" + prev)
            for idx, char in enumerate(prev):
                if char == "(":
                    result.add(prev[:idx+1] + "()" + prev[idx+1:])
        return list(result)
        
        
        