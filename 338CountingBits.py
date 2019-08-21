class Solution:
    def countBits(self, num: int) -> List[int]:
        table = [0 for i in range(num+1)]
        for idx in range(1, num+1):
            if idx %2 == 1:
                table[idx] = table[idx//2]+1
            else:
                table[idx] = table[idx//2]
        return table
        