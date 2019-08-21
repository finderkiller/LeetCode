class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        table = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        
        table[0][0] = True
        for col in range(1,len(table[0])):
            pattern_index = col-1
            if p[pattern_index] == "*":
                table[0][col] = table[0][col-2] if col-2 >=0 else False
        
        for row in range(1,len(table)):
            for col in range(1,len(table[0])):
                string_index = row-1
                pattern_index = col-1
                if p[pattern_index] == s[string_index] or p[pattern_index] == ".":
                    table[row][col] = table[row-1][col-1]
                elif p[pattern_index] == "*":
                    table[row][col] = table[row][col-2]
                    if p[pattern_index-1] == s[string_index] or p[pattern_index-1] == ".":
                        table[row][col] |= table[row-1][col]
        return table[len(s)][len(p)]
                