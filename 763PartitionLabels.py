#Back tracking O(n**n)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        collect = []
        result = []
        self.helper(collect, S, 0, result)
        max_split = max([len(array) for array in result])
        for array in result:
            if len(array) == max_split:
                result = []
                for string in array:
                    result.append(len(string))
                return result
        
    def helper(self, collect, S, start, result):
        if start == len(S):
            result.append(list(collect))
            return
        string = ""
        for idx in range(start, len(S)):
            char = S[idx]
            if char in ''.join(collect):
                return
            string += char
            collect.append(string)
            self.helper(collect, S, idx+1, result)
            collect.pop()
#Greedy O(n)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = {c: idx for idx, c in enumerate(S)}
        left = right = 0
        result = []
        for idx, char in enumerate(S):
            right = max(right, last_index.get(char))
            if idx == right:
                result.append(right-left+1)
                left = right+1
        return result