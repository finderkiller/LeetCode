#sol1: time: O(n) for init, O(n) for dot product, space: O(1)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(vec.nums) != len(self.nums):
            return 0
        result = 0
        for idx in range(len(vec.nums)):
            result += vec.nums[idx] * self.nums[idx]
        return result            

#sol3, time: O(n) for init, O(L1+L2) for dot product
#space: O(L)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = []
        for idx, num in enumerate(nums):
            if num == 0:
                continue
            self.array.append((idx, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        idx = 0
        idj = 0
        result = 0
        while idx < len(self.array) and idj < len(vec.array):
            if self.array[idx][0] == vec.array[idj][0]:
                result += self.array[idx][1] * vec.array[idj][1]
                idx += 1
                idj += 1
            elif self.array[idx][0] < vec.array[idj][0]:
                idx += 1
            else:
                idj += 1
        return result