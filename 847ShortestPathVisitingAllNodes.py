#time: O(n*2^n), since there have n*2^n states
#space: O(n*2^n)
"""
1. queue initialize by pushing all node, step = 0
2. BFS
3. state (cur_node, visted_nodes_status)
4. visited_node_status represented by bitmask
    if cur_node visited: continue
    if visited_nodes_status: 1111 return step
"""
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nodes_count = len(graph)
        all_visited_mask = (1<<nodes_count)-1
        visited = set()
        queue = []
        for idx in range(len(graph)):
            queue.append((idx, 1<<idx))
            visited.add((idx, 1<<idx))
        step = 0
        while len(queue) > 0:
            next_queue = []
            for node, state in queue:
                if state == all_visited_mask:
                    return step
                for neighbor in graph[node]:
                    if (neighbor, state | 1<<neighbor) in visited:
                        continue
                    next_queue.append((neighbor, state | 1<<neighbor))
                    visited.add((neighbor, state | 1<<neighbor))
            queue = next_queue
            step += 1
        return -1
    