class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        result = 0
        while len(arr) > 1:
            min_index = arr.index(min(arr))
            if min_index == 0:
                result += arr[min_index] * arr[min_index+1]
            elif min_index == len(arr)-1:
                result += arr[min_index-1] * arr[min_index]
            else:
                result += arr[min_index]*min(arr[min_index-1], arr[min_index+1])
            arr.pop(min_index)
        return result