#time : O(nlogn), time: O(n)
class Solution:
    def reorganizeString(self, s: str) -> str:
        count_table = {}
        for letter in s:
            if letter not in count_table:
                count_table[letter] = 0
            count_table[letter] += 1
    
        max_heap = []
        result = ""
        import heapq
        for letter, count in count_table.items():
            heapq.heappush(max_heap, (-count, letter))
            
        max_count = -max_heap[0][0]
        if max_count > (len(s)+1)//2:
            return ""
        while len(max_heap) > 1:
            pop_item_first = heapq.heappop(max_heap)
            count_first = -pop_item_first[0]
            letter_first = pop_item_first[1]
            result += letter_first
            
            pop_item_second = heapq.heappop(max_heap)
            count_second = -pop_item_second[0]
            letter_second = pop_item_second[1]
            result += letter_second
            
            if count_first - 1 > 0:
                heapq.heappush(max_heap, (-count_first+1, letter_first))
            if count_second - 1 > 0:
                heapq.heappush(max_heap, (-count_second+1, letter_second))
        if len(max_heap) > 0:
            result += max_heap[0][1]
        return result