#! /usr/bin/python3
import sys

class Solution:
    def __init__(self):
        return
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        return self.searchImpl(nums, 0, len(nums)-1, target)
    def searchImpl(self, nums, start, end, target):
        if end < start:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[start] < nums[mid]:
            if ((target < nums[mid]) and (target >= nums[start])):
                return self.searchImpl(nums, start, mid-1, target)
            else:
                return self.searchImpl(nums, mid+1, end, target)
        else:
            if (target > nums[mid] and target <= nums[end]):
                return self.searchImpl(nums, mid+1, end, target)
            else:
                return self.searchImpl(nums, start, mid-1, target)

def main(argv):
    input = []
    for data in argv[1].split(','):
        input.append(int(data))

    s = Solution()
    print(s.search(input, int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
