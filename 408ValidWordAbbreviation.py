#time: O(n), space: O(n)
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word or not abbr:
            return False
        string = ""
        idx = 0
        current_number = 0
        while idx < len(abbr):
            if self.is_digit(abbr[idx]):
                if current_number == 0 and abbr[idx] == '0':
                    return False
                current_number = 10*current_number + int(abbr[idx])
            else:
                string += ''.join(["*" for i in range(current_number)]) + abbr[idx]
                current_number = 0
            idx += 1
        string += ''.join(["*" for i in range(current_number)])
        if len(string) != len(word):
            return False
        idx = 0
        while idx < len(word):
            if string[idx] != "*" and string[idx] != word[idx]:
                return False
            idx += 1
        return True
    def is_digit(self, char):
        return ord(char) >= ord('0') and ord(char) <= ord('9')

#time: O(n), space: O(1):
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word or not abbr:
            return False
        idx = 0
        idj = 0
        current_number = 0
        while idj < len(abbr):
            if self.is_digit(abbr[idj]):
                if current_number == 0 and abbr[idj] == '0':
                    return False
                current_number = current_number*10 + int(abbr[idj])
                idj += 1
            else:
                idx += current_number
                current_number = 0
                if idx >= len(word) or word[idx] != abbr[idj]:
                    return False
                idx += 1
                idj += 1
        idx += current_number
        return idx == len(word)
            
    def is_digit(self, char):
        return ord(char) >= ord('0') and ord(char) <= ord('9')