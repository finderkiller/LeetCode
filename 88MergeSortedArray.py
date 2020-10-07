class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_last_idx = len(nums1)-1
        first_last_idx = m-1
        second_last_idx = n-1
        while first_last_idx >= 0 and second_last_idx >=0 and total_last_idx >= 0:
            if nums1[first_last_idx] > nums2[second_last_idx]:
                nums1[total_last_idx] = nums1[first_last_idx]
                first_last_idx -= 1
            else:
                nums1[total_last_idx] = nums2[second_last_idx]
                second_last_idx -= 1
            total_last_idx -= 1
        while first_last_idx >= 0 and total_last_idx >= 0:
            nums1[total_last_idx] = nums1[first_last_idx]
            first_last_idx -= 1
            total_last_idx -= 1
        while second_last_idx >= 0 and total_last_idx >= 0:
            nums1[total_last_idx] = nums2[second_last_idx]
            second_last_idx -= 1
            total_last_idx -= 1