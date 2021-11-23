#min_heap,
#time: O(n*k*log(n))
#space: O(n)
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if not primes:
            return 0
        min_heap = [1]
        import heapq
        seen = set()
        for idx in range(n-1):
            min_value = heapq.heappop(min_heap)
            for prime_num in primes:
                if min_value*prime_num in seen:
                    continue
                heapq.heappush(min_heap, min_value*prime_num)
                seen.add(min_value*prime_num)
        return heapq.heappop(min_heap)

#find min manually,
#time: O(n*k)
#space: O(k)
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if not primes:
            return 0
        result = [1]
        num_list = [0 for i in range(len(primes))]
        while n > 1:
            min_value = sys.maxsize
            candidate_index = -1
            for idx, prime in enumerate(primes):
                if  prime*result[num_list[idx]] < min_value:
                    min_value = prime*result[num_list[idx]]
                    candidate_index = idx
            if min_value != result[-1]:
                result.append(min_value)
                n -= 1
            num_list[candidate_index] += 1
        return result[-1]