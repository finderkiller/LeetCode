class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, task in enumerate(tasks):
            task.append(idx)
        tasks.sort(key = lambda x:x[0])
        result = []
        import heapq
        min_heap= []
        time = 0
        idx = 0
        
        while len(min_heap) > 0 or idx < len(tasks):
            while idx < len(tasks) and tasks[idx][0] <= time:
                heapq.heappush(min_heap, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            if not min_heap:
                time = tasks[idx][0]
            else:
                processingTime, index = heapq.heappop(min_heap)
                time += processingTime
                result.append(index)
        return result