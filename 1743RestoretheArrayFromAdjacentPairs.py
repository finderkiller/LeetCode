#time: O(n), extra: O(n), depth: O(n) 
"""
1. build graph
2. find edge
3. DFS collect
"""
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        count_table = {}
        depend_table = {}
        for num1, num2 in adjacentPairs:
            if num1 not in count_table:
                count_table[num1] = 0
            count_table[num1] += 1
            if num2 not in count_table:
                count_table[num2] = 0
            count_table[num2] += 1
            if num1 not in depend_table:
                depend_table[num1] = []
            depend_table[num1].append(num2)
            if num2 not in depend_table:
                depend_table[num2] = []
            depend_table[num2].append(num1)
            
        edge = None
        for key, value in count_table.items():
            if value == 1:
                edge = key
        visited = set()
        result = []
        self.helper(visited, edge, depend_table, result)
        return result
    def helper(self, visited, num, depend_table, result):
        visited.add(num)
        result.append(num)
        for nearby in depend_table.get(num, []):
            if nearby in visited:
                continue
            self.helper(visited, nearby, depend_table, result)
            
            