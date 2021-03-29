class LargestNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_num = sorted(map(str, nums), key=LargestNumKey)
        result = ''.join(sorted_num)
        return result if result[0] != '0' else '0'