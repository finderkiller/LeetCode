class Solution(object):
    def minDominoRotations(self, A, B):
        if not A or not B:
            return -1
        a = A[0]
        b = B[0]
        count_a = 0
        count_b = 0
        for idx in range(len(A)):
            if A[idx] != a and B[idx] != a:
                break
            if A[idx] == a:
                count_a += 1
            if B[idx] == a:
                count_b += 1
            if idx == len(A) - 1:
                return min(len(A)-count_a, len(B)-count_b)
        count_a = 0
        count_b = 0
        for idx in range(len(B)):
            if A[idx] != b and B[idx] != b:
                break
            if A[idx] == b:
                count_a += 1
            if B[idx] == b:
                count_b += 1
            if idx == len(B) - 1:
                return min(len(A)-count_a, len(B)-count_b)
        return -1