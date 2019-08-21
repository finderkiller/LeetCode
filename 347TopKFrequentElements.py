class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        result = []
        table = {}
        for num in nums:
            value = table.get(num,0)
            table[num] = value + 1
        keylist = sorted(table, key=table.get, reverse=True)
        
        return keylist[:k]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        if not nums or k <= 0:
            return []
        freq_table = {}
        min_heap = []
        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1
        
        for key, value in freq_table.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return reversed([tuple[1] for tuple in min_heap])        