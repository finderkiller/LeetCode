#time: O(n), space: O(1)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or not order:
            return False
        self.order = order
        for idx in range(1, len(words)):
            if not self.isSmaller(words[idx-1], words[idx]):
                return False
        return True
        
    def isSmaller(self, string1, string2):
        idx = 0
        idj = 0
        while idx < len(string1) and idj < len(string2):
            if self.order.find(string1[idx]) < self.order.find(string2[idj]):
                return True
            elif self.order.find(string1[idx]) > self.order.find(string2[idj]):
                return False
            idx += 1
            idj += 1
        return len(string2) >= len(string1)
#time: O(n), space: O(26), build order table
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or not order:
            return False
        self.order = {}
        for idx in range(len(order)):
            self.order[order[idx]] = idx
    
        for idx in range(1, len(words)):
            if not self.isSmaller(words[idx-1], words[idx]):
                return False
        return True
        
    def isSmaller(self, string1, string2):
        idx = 0
        idj = 0
        while idx < len(string1) and idj < len(string2):
            if self.order.get(string1[idx]) < self.order.get(string2[idj]):
                return True
            elif self.order.get(string1[idx]) > self.order.get(string2[idj]):
                return False
            idx += 1
            idj += 1
        return len(string2) >= len(string1)