class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for idx, num in enumerate(nums):
            if num in table and abs(table[num]-idx) <= k:
                return True
            table[num] = idx
        return False