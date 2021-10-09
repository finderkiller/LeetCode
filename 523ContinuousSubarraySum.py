class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if k == 0:
            return False
        table = {}
        cur_sum = 0
        table[0] = -1
        for idx, num in enumerate(nums):
            cur_sum += num
            if cur_sum not in table:
                table[cur_sum] = idx
            max_num = cur_sum//k
            for multiple_num in range(max_num, -1, -1):
                if (cur_sum - multiple_num*k) in table and \
                idx - table[(cur_sum - multiple_num*k)] > 1:
                    return True
        return False