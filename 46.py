#! /usr/local/bin/python3
import sys


class Solution:
    def __init__(self):
        return
    def permute(self, nums):
        result = []
        prefix = []
        self.permuteImpl(prefix, nums, result)
        return result
    def permuteImpl(self, prefix, remainder, result):
        if (len(remainder) == 0):
            result.append(prefix)
            return
        for idx, value in enumerate(remainder):
            before = remainder[:idx]
            after = remainder[idx+1:]
            next = list(prefix)
            next.append(value)
            self.permuteImpl(next, before+after, result)
        return 

def main(argv):
    input = []
    s = Solution()

    for data in sys.argv[1].split(','):
        input.append(int(data))
    print(s.permute(input))

if __name__ == "__main__":
    main(sys.argv)