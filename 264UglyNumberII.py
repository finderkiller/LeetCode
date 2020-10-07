#heap, set
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return
        heap = [1]
        seen = set()
        import heapq
        for i in range(n-1):
            min = heapq.heappop(heap)
            if min*2 not in seen:
                heapq.heappush(heap, min*2)
                seen.add(min*2)
            if min*3 not in seen:  
                heapq.heappush(heap, min*3)
                seen.add(min*3)
            if min*5 not in seen:
                heapq.heappush(heap, min*5)
                seen.add(min*5)
        return heapq.heappop(heap)
#DP
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return
        i2 = i3 = i5 = 0
        result = [1]
        for idx in range(1, n):
            num = min(result[i2]*2, result[i3]*3, result[i5]*5)
            result.append(num)
            if num == result[i2]*2:
                i2 += 1
            if num == result[i3]*3:
                i3 += 1
            if num == result[i5]*5:
                i5 += 1
        
        return result[-1]