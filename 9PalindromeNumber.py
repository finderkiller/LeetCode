class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        input = []
        while x !=0:
            input.append(x%10)
            x = x // 10
        left = 0
        right = len(input)-1
        while left <= right:
            if input[left] != input[right]:
                return False
            left +=1
            right -=1
        return True