# time: O(nlogn), space: O(n)
"""
1. sorted
2. build count hash table
3. traverse again, if count > 0, finding their double, if found double, table[double] -= 1
    and append value to result
4. return result

case
1. [0, 0, 0]
table = {0: 0}
result = [0, ]

2. [0, 0, 0, 0]
table = {0: 4}
result = [0, 0]

3. [1,3,4,2,6,8]
table = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    6: 0,
    8: 0
    }
result = [1, 3, 4]
"""
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count_table = {}
        result = []
        for num in changed:
            if num not in count_table:
                count_table[num] = 0
            count_table[num] += 1
        
        for num in changed:
            if count_table[num] == 0:
                continue
            count_table[num] -= 1
            double = 2*num
            if double not in count_table:
                return []
            if count_table[double] < 1:
                return []
            count_table[double] -= 1
            result.append(num)
        return result