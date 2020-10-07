#brute force
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        table = [[False, False] for i in range(len(A))]
        table[-1][0] = True
        table[-1][1] = True
        ans = 1
        for i in range(len(table)-2, -1, -1):
            upper_bound = sys.maxsize
            lower_bound = -sys.maxsize
            upper_bound_idx = -1
            lower_bound_idx = -1
            for idx in range(i+1, len(table)):
                if A[idx] >= A[i] and A[idx] < upper_bound:
                    upper_bound = A[idx]
                    upper_bound_idx = idx
                if A[idx] <= A[i] and A[idx] > lower_bound:
                    lower_bound = A[idx]
                    lower_bound_idx = idx
            if upper_bound_idx != -1:
                table[i][0] = table[upper_bound_idx][1]
            if lower_bound_idx != -1:
                table[i][1] = table[lower_bound_idx][0]
            if table[i][0]:
                ans += 1
        return ans

#using binary search to find lowerbound and upperbound
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import bisect
        if not A:
            return 0
        table = [[False, False] for i in range(len(A))]
        table[-1][0] = True
        table[-1][1] = True
        array = [A[-1]]
        index_map = {}
        index_map[A[-1]] = len(A)-1
        ans = 1
        for i in range(len(table)-2, -1, -1):
            upper_insert_point = bisect.bisect_left(array, A[i])
            if upper_insert_point < len(array):
                upper_bound_idx = index_map[array[upper_insert_point]]
                table[i][0] = table[upper_bound_idx][1]
            lower_insert_point = bisect.bisect_right(array, A[i])
            if lower_insert_point > 0:
                lower_bound_idx = index_map[array[lower_insert_point-1]]
                table[i][1] = table[lower_bound_idx][0]
            if table[i][0]:
                ans += 1
            if upper_insert_point == len(array) or array[upper_insert_point] != A[i]:
                array.insert(upper_insert_point, A[i])
            index_map[A[i]] = i
        return ans