"""
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for letter in columnTitle:
            num = ord(letter)-ord('A')+1
            result = 26*result + num
        return result