class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = (10**9+7)
        if N <0:
            return 0
        table = [1 for i in range(10)]
        for step in range(N-1):
            next_table = [0 for i in range(10)]
            for next_idx in range(len(next_table)):
                if next_idx == 1:
                    next_table[next_idx] = table[6]+table[8]
                if next_idx == 2:
                    next_table[next_idx] = table[7]+table[9]
                if next_idx == 3:
                    next_table[next_idx] = table[4]+table[8]
                if next_idx == 4:
                    next_table[next_idx] = table[3]+table[9]+table[0]
                if next_idx == 6:
                    next_table[next_idx] = table[1]+table[7]+table[0]
                if next_idx == 7:
                    next_table[next_idx] = table[2]+table[6]
                if next_idx == 8:
                    next_table[next_idx] = table[1]+table[3]
                if next_idx == 9:
                    next_table[next_idx] = table[2]+table[4]
                if next_idx == 0:
                    next_table[next_idx] = table[4]+table[6]
            table = next_table            
        return sum(table)%mod