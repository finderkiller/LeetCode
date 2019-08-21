class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)
        length = len(merged)
        if length % 2 == 0:
            return (merged[length//2] + merged[length//2 -1])/2
        return merged[length//2]
    
    def merge(self, nums1, nums2):
        result = []
        idx1 = 0
        idx2 = 0
        while idx1 < len(nums1) or idx2 < len(nums2):
            if idx1 == len(nums1):
                result.append(nums2[idx2])
                idx2 += 1
                continue
            if idx2 == len(nums2):
                result.append(nums1[idx1])
                idx1 += 1
                continue
            if nums1[idx1] < nums2[idx2]:
                result.append(nums1[idx1])
                idx1 += 1
            else:
                result.append(nums2[idx2])
                idx2 += 1
        return result

#binary seasrch
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