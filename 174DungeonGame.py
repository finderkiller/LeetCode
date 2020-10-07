class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        table = [[0 for i in range(len(dungeon[0]))] for i in range(len(dungeon))]
        for row in range(len(table)-1, -1, -1):
            for col in range(len(table[0])-1, -1, -1):
                if row == len(table)-1 and col == len(table[0])-1:
                    table[row][col] = max(1, 1-dungeon[-1][-1])
                    continue
                right = table[row][col+1] if col+1 < len(table[0]) else sys.maxsize
                down = table[row+1][col] if row+1 < len(table) else sys.maxsize
                table[row][col] = max(1, min(right, down)-dungeon[row][col])
        return table[0][0]
        