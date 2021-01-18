#max_heap O(nlogk)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        max_heap = []
        result = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heapq.heappush(max_heap, (-distance, x, y))
            if len(max_heap) > K:
                heapq.heappop(max_heap)
        while len(max_heap) > 0:
            neg_distance, x, y = heapq.heappop(max_heap)
            result.append([x, y])
        return result

#quick selectionm, O(n)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_w_point_list = []
        result = []
        for x, y in points:
            distance_w_point_list.append((sqrt(x**2+y**2), x, y))
        self.helper(distance_w_point_list, 0, len(distance_w_point_list)-1, K)
        while K > 0:
            x = distance_w_point_list[K-1][1]
            y = distance_w_point_list[K-1][2]
            result.append([x, y])
            K -= 1
        return result
    def helper(self, distance_w_point_list, start, end, K):
        if start == end:
            return
        pivot_idx = random.randint(start, end)
        pivot_value = distance_w_point_list[pivot_idx][0]
        self.swap(distance_w_point_list, pivot_idx, end)
        i = start - 1
        for j in range(start, end):
            if distance_w_point_list[j][0] < pivot_value:
                i += 1
                self.swap(distance_w_point_list, i, j)
        i += 1
        self.swap(distance_w_point_list, i, end)
        if i == K-1:
            return
        elif i < K-1:
            self.helper(distance_w_point_list, i+1, end, K)
        else:
            self.helper(distance_w_point_list, start, i-1, K)
        
    def swap(self, array, idx_a, idx_b):
        tmp = array[idx_a]
        array[idx_a] = array[idx_b]
        array[idx_b] = tmp
        class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_w_point_list = []
        result = []
        for x, y in points:
            distance_w_point_list.append((sqrt(x**2+y**2), x, y))
        self.helper(distance_w_point_list, 0, len(distance_w_point_list)-1, K)
        while K > 0:
            x = distance_w_point_list[K-1][1]
            y = distance_w_point_list[K-1][2]
            result.append([x, y])
            K -= 1
        return result
    def helper(self, distance_w_point_list, start, end, K):
        if start == end:
            return
        pivot_idx = random.randint(start, end)
        pivot_value = distance_w_point_list[pivot_idx][0]
        self.swap(distance_w_point_list, pivot_idx, end)
        i = start - 1
        for j in range(start, end):
            if distance_w_point_list[j][0] < pivot_value:
                i += 1
                self.swap(distance_w_point_list, i, j)
        i += 1
        self.swap(distance_w_point_list, i, end)
        if i == K-1:
            return
        elif i < K-1:
            self.helper(distance_w_point_list, i+1, end, K)
        else:
            self.helper(distance_w_point_list, start, i-1, K)
        
    def swap(self, array, idx_a, idx_b):
        tmp = array[idx_a]
        array[idx_a] = array[idx_b]
        array[idx_b] = tmp