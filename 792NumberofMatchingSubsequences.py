
#brute force O(n*s+n*L), n is the length of words, s is the length of s
# 1. traverse all words
# 2. each word, two pointer for letter and s
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        for word in words:
            idx = 0
            idj = 0
            while idx < len(word) and idj < len(s):
                if word[idx] == s[idj]:
                    if idx == len(word)-1:
                        result += 1
                    idx += 1
                    idj += 1
                elif word[idx] != s[idj]:
                    idj += 1
        return result

#time: O(n*L + s*n*L), space: O(n*L)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        table = {}
        for word in words:
            if word[0] not in table:
                table[word[0]] = []
            table[word[0]].append(word)
            
        for letter in s:
            if letter not in table:
                continue
            word_list = table.get(letter)
            table.pop(letter)
            for word in word_list:
                if len(word) == 1:
                    result += 1
                    continue
                if word[1] not in table:
                    table[word[1]] = []
                table[word[1]].append(word[1:])
        return result


#time: O(n*L + s*n), space: O(n*L)
# worst case, when words are all the same with S, O(n*L + s*n)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        table = {}
        for word in words:
            it = iter(word)
            first_letter = next(it)
            if first_letter not in table:
                table[first_letter] = []
            table[first_letter].append(it)
            
        for letter in s:
            if letter not in table:
                continue
            it_list = table.get(letter)
            table.pop(letter)
            for it in it_list:
                next_letter = next(it, None)
                if not next_letter:
                    result += 1
                    continue
                if next_letter not in table:
                    table[next_letter] = []
                table[next_letter].append(it)
        return result