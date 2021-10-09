#time: O(n), space: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr:
            return k
        missing_count = arr[0]-1
        if k > missing_count:
            k -= missing_count
        else:
            return k

        for idx in range(1, len(arr)):
            missing_count = arr[idx]-arr[idx-1]-1
            if k > missing_count:
                k -= missing_count
            else:
                return arr[idx-1]+k
        return arr[-1]+k