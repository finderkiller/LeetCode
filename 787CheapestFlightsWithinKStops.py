"""
1. build graph (src, dst): price
2. DFS with step: from ori_src, 
3. DFS(node, target, current_price, step)
if node == dst:
        update cheapest price
    if node > k:
        return
        
"""
#time: O(flights^(station*steps))
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.table = {}
        for a, b, price in flights:
            if a not in self.table:
                self.table[a] = {}
            self.table[a][b] = price
        
        self.result = sys.maxsize
        self.helper(src, dst, 0, k+1)
        return self.result if self.result != sys.maxsize else -1
    
    def helper(self, node, target, cur_price, step):
        if node == target:
            self.result = min(self.result, cur_price)
            return
        if step == 0:
            return
        if node not in self.table:
            return
        for next_node, price in self.table.get(node).items():
            self.helper(next_node, target, cur_price+price, step-1)

#time: O(station*steps*flights)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.table = {}
        for a, b, price in flights:
            if a not in self.table:
                self.table[a] = {}
            self.table[a][b] = price
        self.memo = {}
        result = self.helper(src, dst, k+1)
        return result if result != sys.maxsize else -1
    
    def helper(self, node, target, step):
        if node == target:
            return 0
        if step == 0:
            return sys.maxsize
        if node not in self.table:
            return sys.maxsize
        if (node, step) in self.memo:
            return self.memo[(node, step)]
        result = sys.maxsize
        for next_node, price in self.table.get(node).items():
            forward = self.helper(next_node, target, step-1)
            result = min(result, price + forward)
        self.memo[(node, step)] = result
        return result