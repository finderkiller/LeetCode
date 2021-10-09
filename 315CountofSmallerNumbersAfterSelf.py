class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = []
        sorted_list = []
        import bisect
        for num in nums[::-1]:
            insert_index = bisect.bisect_left(sorted_list, num)
            sorted_list.insert(insert_index, num)
            result.append(insert_index)
        return result[::-1]