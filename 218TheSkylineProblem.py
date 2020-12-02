class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        input = []
        max_heap = []
        result = []
        cur_height = 0
        pre_height = 0
        import heapq
        heapq.heappush(max_heap, 0)
        for building in buildings:
            left = building[0]
            right = building[1]
            height = building[2]
            input.append((left, -height))
            input.append((right, height))
        input.sort(key = lambda x:(x[0], x[1]))
        for x, y in input:
            if y < 0:
                heapq.heappush(max_heap, y)
            else:
                #delete height from heap
                idx = max_heap.index(-y)
                max_heap.pop(idx)
                heapq.heapify(max_heap)
            cur_height = -max_heap[0]
            if cur_height != pre_height:
                result.append([x, cur_height])
                pre_height = cur_height
        return result

# enhance deleting height from heap, using dict
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        input = []
        delete_table = {}
        max_heap = []
        result = []
        cur_height = 0
        pre_height = 0
        import heapq
        heapq.heappush(max_heap, 0)
        for building in buildings:
            left = building[0]
            right = building[1]
            height = building[2]
            input.append((left, -height))
            input.append((right, height))
        input.sort(key = lambda x:(x[0], x[1]))
        for x, y in input:
            if y < 0:
                heapq.heappush(max_heap, y)
            else:
                #delete height from heap
                delete_table[y] = delete_table.get(y, 0) + 1
                while max_heap and delete_table.get(-max_heap[0], 0) != 0:
                    delete_table[-max_heap[0]] = delete_table.get(-max_heap[0], 0) - 1
                    heapq.heappop(max_heap)
            cur_height = -max_heap[0]
            if cur_height != pre_height:
                result.append([x, cur_height])
                pre_height = cur_height
        return result