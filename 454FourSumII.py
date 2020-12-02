class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        table_ab = {}
        table_cd = {}
        result = 0
        for a in A:
            for b in B:
                table_ab[a+b] = table_ab.get(a+b, 0) + 1
            
        for c in C:
            for d in D:
                table_cd[c+d] = table_cd.get(c+d, 0) + 1
        
        for cd_sum, value in table_cd.items():
            key = 0-cd_sum
            result += table_ab.get(key, 0) * value
        return result