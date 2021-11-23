"""
1. server stored as min_heap by (weight, idx)
2. used_server stored as min_heap by (end_time, weight, idx)
3. traverse task
    1. see used_server, checking ended server, pop from used_server and push to server
    2. task pick server and have the end_time of that server, push to used_server
"""
#two min_heap
#time: O(nlogk), space: O(k), k server, n task
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        import heapq
        available_server = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available_server)
        used_server = []
        
        result = []
        time = 0
        for start_time, time_cost in enumerate(tasks):
            time = max(time, start_time)
            if len(available_server) == 0:
                time = used_server[0][0]
            while len(used_server) > 0 and used_server[0][0] <= time:
                end_time, wight, idx = heapq.heappop(used_server)
                heapq.heappush(available_server, (wight, idx))
            weight, idx = heapq.heappop(available_server)
            result.append(idx)
            heapq.heappush(used_server, (time+time_cost, weight, idx))
        return result