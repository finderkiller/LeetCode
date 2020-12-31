class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = set()
        result = set()
        for data in nums1:
            table.add(data)
        for data in nums2:
            if data in table:
                result.add(data)
        return list(result)