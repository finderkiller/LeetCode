class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)
        start = 0
        end = x
        while start <= end:
            partitionx = (start + end)//2
            partitiony = (x+y)//2 - partitionx
            xleftmax = nums1[partitionx-1] if partitionx != 0 else -sys.maxsize-1
            xrightmin = nums1[partitionx] if partitionx != x else sys.maxsize
            
            yleftmax = nums2[partitiony-1] if partitiony != 0 else -sys.maxsize-1
            yrightmin = nums2[partitiony] if partitiony != y else sys.maxsize
            
            if xleftmax <= yrightmin and yleftmax <= xrightmin:
                if (x+y)%2 == 0:
                    return (max(xleftmax, yleftmax) + min(xrightmin, yrightmin))/2
                else:
                    return min(xrightmin, yrightmin)
            elif xleftmax > yrightmin:
                end = partitionx - 1
            else:
                start= partitionx + 1
        return None