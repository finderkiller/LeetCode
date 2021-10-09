class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        if not sentence:
            return ""
        word_list = sentence.split(' ')
        result = ""
        for idx, word in enumerate(word_list):
            if self.isVowel(word[0].lower()):
                result += word
            else:
                result += word[1:]
                result += word[0]
            result += "ma"
            count = 0
            while count <= idx:
                result += 'a'
                count += 1
            result += " "
            
        return result[:-1]
            
    
    def isVowel(self, char):
        return char == "a" or char == "e" or char == "i" or char == "o" or char == "u"