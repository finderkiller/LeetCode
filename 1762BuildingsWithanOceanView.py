#time: O(n), space: O(1)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 0:
            return []
        res = []
        right_max_height = 0
        for idx in range(len(heights)-1, -1, -1):
            if heights[idx] > right_max_height:
                res.append(idx)
                right_max_height = max(right_max_height, heights[idx])
        res.reverse()
        return res