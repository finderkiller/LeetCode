#Recursive
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        return self.helper(s1, s2, s3)
    def helper(self, s1, s2, s3):
        if not s1 and not s2 and not s3:
            return True
        if not s3:
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        return (s1[0] == s3[0] and self.helper(s1[1:], s2, s3[1:])) or (s2[0] == s3[0] and self.helper(s1, s2[1:], s3[1:]))
#memo
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        self.table ={}
        return self.helper(s1, s2, s3)
    def helper(self, s1, s2, s3):
        if not s1 and not s2 and not s3:
            return True
        if not s3:
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if (s1, s2) in self.table:
            return self.table[(s1, s2)]
        self.table[(s1, s2)] = (s1[0] == s3[0] and self.helper(s1[1:], s2, s3[1:])) or (s2[0] == s3[0] and self.helper(s1, s2[1:], s3[1:]))
        return self.table[(s1, s2)]
#DP
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        table = [[False for i in range(len(s1)+1)] for j in range(len(s2)+1)]
        table[0][0] = True
        for col in range(1, len(table[0])):
            string_idx = col-1
            table[0][col] = table[0][col-1] and s1[string_idx] == s3[string_idx]
        for row in range(1, len(table)):
            string_idx = row-1
            table[row][0] = table[row-1][0] and s2[string_idx] == s3[string_idx]
        
        for row in range(1,len(table)):
            for col in range(1,len(table[0])):
                s1_idx = col-1
                s2_idx = row-1
                table[row][col] = (table[row-1][col] and s2[s2_idx] == s3[s1_idx+s2_idx+1]) or (table[row][col-1] and s1[s1_idx] == s3[s1_idx+s2_idx+1])
        return table[-1][-1]