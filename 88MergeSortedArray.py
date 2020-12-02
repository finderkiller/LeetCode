class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_idx = len(nums1)-1
        first_idx = m - 1
        second_idx = n - 1
        
        while first_idx >= 0 or second_idx >= 0:
            if second_idx < 0:
                return
            if first_idx < 0:
                nums1[last_idx] = nums2[second_idx]
                second_idx -= 1
            elif nums1[first_idx] >= nums2[second_idx]:
                nums1[last_idx] = nums1[first_idx]
                first_idx -= 1
            else:
                nums1[last_idx] = nums2[second_idx]
                second_idx -= 1
            last_idx -= 1