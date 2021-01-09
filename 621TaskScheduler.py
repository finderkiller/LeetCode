class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = {}
        for task in tasks:
            table[task] = table.get(task, 0) + 1
        max_freq = max(table.values())
        count = 0
        for key, value in table.items():
            if value == max_freq:
                count += 1
        return max(len(tasks), (max_freq-1)*(n+1)+count)