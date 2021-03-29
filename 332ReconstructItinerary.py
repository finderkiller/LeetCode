class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if len(tickets) == 0:
            return []
        if len(tickets) == 1:
            return [tickets[0][0], tickets[0][1]]
        depend_table = defaultdict(set)
        self.result = []
        self.visited = defaultdict(int)
        for ticket in tickets:
            begin = ticket[0]
            end = ticket[1]
            depend_table[begin].add(end)
            self.visited[(begin, end)] += 1
        if 'JFK' not in depend_table:
            return []
        self.result.append('JFK')
        self.total_tickets = len(tickets)
        if not self.helper('JFK', depend_table, 0):
            return []
        return self.result
        
    def helper(self, airport, depend_table, level):
        if airport not in depend_table:
            return False
        for child in sorted(list(depend_table[airport])):
            if (airport, child) in self.visited and self.visited[(airport, child)] == 0:
                continue
            self.visited[(airport, child)] -= 1
            self.result.append(child)
            if level+1 == self.total_tickets:
                return True
            if self.helper(child, depend_table, level+1):
                return True
            self.result.pop()
            self.visited[(airport, child)] += 1
        return False
        