#DFS

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = {}
        for employee in employees:
            table[employee.id] = employee
        if id not in table:
            return 0
        return self.helper(table.get(id), table)
        
    def helper(self, node, table):
        result = 0
        result += node.importance
        for child in node.subordinates:
            result += self.helper(table.get(child), table)
        return result
        