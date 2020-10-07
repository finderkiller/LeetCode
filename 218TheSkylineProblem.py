class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        height = []
        heap = [0]
        erased = {}
        pre = 0
        cur = 0
        output = []
        for building in buildings:
            height.append([building[0], -building[2]])
            height.append([building[1], building[2]])
        height.sort(key=lambda x:(x[0], x[1]))
        for data in height:
            if data[1] < 0:
                heapq.heappush(heap, data[1])
            else:
                erased[data[1]] = erased.get(data[1], 0) + 1
                while heap and erased.get(-heap[0], 0) != 0:
                    erased[-heap[0]] -= 1
                    heapq.heappop(heap)
            cur = -heap[0]
            if cur != pre:
                output.append([data[0], cur])
                pre = cur
        return output