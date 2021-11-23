#recursive
#time: O(n), depth: O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        self.idx = 0
        return self.helper(s)
        
    def helper(self, s):
        result = ""
        cur_num = 0
        while self.idx < len(s):
            letter = s[self.idx]
            if self.isdigit(letter):
                cur_num = 10*cur_num + int(letter)
                self.idx += 1
            elif letter == "[":
                self.idx += 1
                forword = self.helper(s)
                count = cur_num
                while count > 0:
                    result += forword
                    count -= 1
                cur_num = 0
            elif letter == "]":
                self.idx += 1
                return result
            else:
                result += letter
                self.idx += 1
        return result

def isdigit(self, letter):
        return ord(letter) >= ord('0') and ord(letter) <= ord('9')   
        