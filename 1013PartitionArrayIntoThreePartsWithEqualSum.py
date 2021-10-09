#sol1: using flag
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if not arr:
            return False
        total = sum(arr)
        if total % 3 != 0:
            return False
        first_found = False
        cur_sum = 0
        for idx, num in enumerate(arr):
            cur_sum += num
            if cur_sum == total//3 and not first_found:
                first_found = True
                cur_sum = 0
            elif idx != len(arr)-1 and cur_sum == total//3 and first_found:
                return True
        return False
        

# sol2: using count
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if not arr:
            return False
        total = sum(arr)
        if total % 3 != 0:
            return False
        cur_sum = 0
        count = 0
        for idx, num in enumerate(arr):
            cur_sum += num
            if cur_sum == total//3:
                count += 1
                cur_sum = 0
        return count >= 3
        