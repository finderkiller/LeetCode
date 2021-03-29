class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        left_min_stack = []
        cur_min = -sys.maxsize-1
        for value in preorder:
            if value < cur_min:
                return False
            while left_min_stack and left_min_stack[-1] < value:
                cur_min = left_min_stack.pop()
            left_min_stack.append(value)
        return True