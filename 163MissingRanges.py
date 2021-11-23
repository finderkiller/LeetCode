#time O(n)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        for num in nums:
            if num > lower:
                result.append(str(lower) + ("->" + str(num-1) if (num-1 != lower) else ""))
            if num == upper:
                return result
            lower = num+1
        result.append(str(lower) + ("->" + str(upper) if (upper != lower) else ""))
        return result