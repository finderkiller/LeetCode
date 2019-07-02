class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        index1 = m-1
        index2 = n-1
        lastindex = len(nums1)-1
        
        while index1 >=0 and index2 >=0:
            if nums2[index2] >= nums1[index1]:
                nums1[lastindex] = nums2[index2]
                index2 -=1
            else:
                nums1[lastindex] = nums1[index1]
                index1 -= 1
            lastindex -=1
        
        if index1 == -1:
            while lastindex >= 0 and index2 >=0:
                nums1[lastindex] = nums2[index2]
                lastindex -=1
                index2-=1
        elif index2 == -1:
            while lastindex >= 0 and index1 >=0:
                nums1[lastindex] = nums1[index1]
                lastindex -=1
                index1-=1
