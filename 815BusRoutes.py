"""BFS
1. build depend_table, stop: stops in same route
2. queue, steps
3. return steps
"""
#time: O(m*n), ,space: O(m*n), m routes, n stops
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        self.table = {}
        for route in routes:
            for idx in range(len(route)):
                if route[idx] not in self.table:
                    self.table[route[idx]] = set()
                for stop in route[:idx] + route[idx+1:]:
                    self.table[route[idx]].add(stop)
        queue = []
        queue.append(source)
        visited = set()
        visited.add(source)
        step = 0
        while len(queue) > 0:
            next_queue = []
            for stop in queue:
                if stop == target:
                    return step
                if stop not in self.table:
                    continue
                for next_stop in self.table.get(stop):
                    if next_stop in visited:
                        continue
                    visited.add(next_stop)
                    next_queue.append(next_stop)
            step += 1
            queue = next_queue
        return -1

"""BFS
1. build invert depend_table, stop: route_idx
2. queue, steps
3. return steps
"""
#time: O(m*n), ,space: O(m*n), m routes, n stops
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        self.table = {}
        for idx in range(len(routes)):
            route = routes[idx]
            for stop in route:
                if stop not in self.table:
                    self.table[stop] = []
                self.table[stop].append(idx)
        
        queue = [source]
        visited = set()
        step = 0
        while len(queue) > 0:
            step += 1
            next_queue = []
            for stop in queue:
                for route_idx in self.table[stop]:
                    if route_idx in visited:
                        continue
                    visited.add(route_idx)
                    for next_stop in routes[route_idx]:
                        if next_stop == target:
                            return step
                        next_queue.append(next_stop)
            queue = next_queue
        return -1