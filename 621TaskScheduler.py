class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        table = {}
        for task in tasks:
            table[task] = table.get(task, 0) + 1
        tuple_list = sorted(table.items(), key=lambda x:x[1], reverse=True)
        max_frequency = tuple_list[0][1]
        i = 0
        while i < len(tuple_list) and tuple_list[i][1] == max_frequency:
            i += 1   
        return max(len(tasks),((max_frequency-1) * (n+1) + i))
        