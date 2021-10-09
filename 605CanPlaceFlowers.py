
#O(n)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        index = 0
        while index < len(flowerbed):
            if n == 0:
                return True
            plantBefore = index > 0 and flowerbed[index-1] == 1
            plantAfter = index+1 < len(flowerbed) and flowerbed[index+1] == 1
            if not plantBefore and not plantAfter and flowerbed[index] == 0:
                flowerbed[index] = 1
                n -= 1
            index += 1
        return n == 0