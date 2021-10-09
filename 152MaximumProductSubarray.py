
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        max_product = -sys.maxsize-1
        prev_min_product = 1
        prev_max_product = 1
        for value in nums:
            cur_min_product = min(value*prev_min_product, value*prev_max_product, value)
            cur_max_product = max(value*prev_min_product, value*prev_max_product, value)
            max_product = max(cur_max_product, max_product)
            prev_min_product = cur_min_product
            prev_max_product = cur_max_product
        return max_product
        