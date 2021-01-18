class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        table = {}
        first = self.getNext(cells)
        next_day = self.getNext(first)
        table[1] = first
        day = 2
        while next_day != first:
            table[day] = next_day
            next_day = self.getNext(next_day)
            day += 1
        return table.get(N%(day-1)) if N%(day-1) != 0 else table[day-1]
        
    def getNext(self, cells):
        result = []
        for idx in range(len(cells)):
            if idx == 0 or idx == 7:
                result.append(0)
            elif cells[idx+1] == cells[idx-1]:
                result.append(1)
            else:
                result.append(0)
        return result
        