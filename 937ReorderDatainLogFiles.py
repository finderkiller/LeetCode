class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = []
        alph = []
        for data in logs:
            idf, log = data.split(' ', 1)
            if log[0].isdigit():
                nums.append(data)
            else:
                alph.append(data)
        alph.sort(key = lambda x:(x.split(' ', 1)[1], x.split(' ', 1)[0]))
        return alph+nums
        