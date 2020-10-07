class Solution:
    def isUgly(self, num: int) -> bool:
        if num <=0:
            return False
        if num <= 6:
            return True
        while num >0:
            if num%2 != 0:
                break
            num = num//2
        
        while num > 0:
            if num %3 !=0:
                break
            num = num//3
        while num > 0:
            if num %5 !=0:
                break
            num = num//5
        return num == 1
        