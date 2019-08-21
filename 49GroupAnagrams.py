class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        table = {}
        ret = []
        for string in strs:
            key = "".join(sorted(string))
            if key not in table:
                table[key] = [string]
            else:
                table[key].append(string)
        for key, value in table.items():
            ret.append(value)
        return ret
        