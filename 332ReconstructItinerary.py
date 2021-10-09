#time:O(n), n is the number of tickets, space: O(n), child_table
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        child_table = {}
        for ticket in tickets:
            src = ticket[0]
            des = ticket[1]
            if src not in child_table:
                child_table[src] = {}
            if des not in child_table[src]:
                child_table[src][des] = 0
            child_table[src][des] += 1
        self.result = []
        self.result.append("JFK")
        if not self.helper(tickets, "JFK", child_table, 0):
            return []
        return self.result
    
    def helper(self, tickets, src, child_table, level):
        if len(tickets) == level:
            return True
        if src not in child_table:
            return False
        for des in sorted(child_table[src].keys()):
            if child_table[src][des] == 0:
                continue
            child_table[src][des] -= 1
            self.result.append(des)
            if self.helper(tickets, des, child_table, level+1):
                return True
            self.result.pop()
            child_table[src][des] += 1
        return False