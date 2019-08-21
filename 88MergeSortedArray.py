class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_index = len(nums1)-1
        nums1_index = m-1
        nums2_index = n-1
        while last_index >= 0:
            if nums1_index < 0:
                nums1[last_index] = nums2[nums2_index]
                nums2_index -= 1
            elif nums2_index < 0:
                nums1[last_index] = nums1[nums1_index]
                nums1_index -= 1
            elif  nums1[nums1_index] >= nums2[nums2_index]:
                nums1[last_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[last_index] = nums2[nums2_index]
                nums2_index -= 1
            last_index -= 1
        