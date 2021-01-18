#sort, time:O(nlogn)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        table = defaultdict(int)
        for word in words:
            table[word] += 1
            
        sorted_list = sorted(table.items(), key = lambda x:(-x[1],x[0]))
        while k > 0:
            result.append(sorted_list[0][0])
            sorted_list.pop(0)
            k -= 1
        return result

#min_heap, customize the element in heap for comparing, time:O(nlogk)
class HeapElement:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        result = []
        table = defaultdict(int)
        for word in words:
            table[word] += 1
        min_heap = []
        for word, count in table.items():
            heapq.heappush(min_heap, (HeapElement(word, count), word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        while len(min_heap):
            result.append(heapq.heappop(min_heap)[1])
        return result[::-1]