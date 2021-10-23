#DFS: time: O(d^E), E is flights, d is the max of departure from an airport
#space: O(E)
"""
1. build tickets table, value: count of tickets
2. traverse, starting from JFK, if no tickets, just skip
3. if len(result) == len(tickets)+1, meaning use all of ticket, then return
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.depend_table = {}
        for src, des in tickets:
            if src not in self.depend_table:
                self.depend_table[src] = {}
            if des not in self.depend_table[src]:
                self.depend_table[src][des] = 0
            self.depend_table[src][des] += 1
        result = []
        result.append("JFK")
        level = len(tickets)+1
        self.helper("JFK", result, level)
        return result
        
    def helper(self, src, result, level):
        if len(result) == level:
            return True
        if src not in self.depend_table:
            return False
        for des in sorted(self.depend_table[src].keys()):
            if self.depend_table[src][des] == 0:
                continue
            self.depend_table[src][des] -= 1
            result.append(des)
            if self.helper(des, result, level):
                return True
            result.pop()
            self.depend_table[src][des] += 1
        return False