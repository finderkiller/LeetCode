class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        result = []
        word_table = {}
        for word in words:
            if word in word_table:
                word_table[word] += 1
            else:
                word_table[word] = 1
        word_length = len(words[0])
        word_number = len(words)
        for idx in range(0, len(s) - word_length*word_number+1, 1):
            word_copy_table = dict(word_table)
            success = True
            for idj in range(idx, idx+word_length*(word_number-1)+1, word_length):
                word = s[idj:idj+word_length]
                if word in word_copy_table and word_copy_table[word] > 0:
                    word_copy_table[word] -= 1
                else:
                    success = False
                    break
            if success:
                result.append(idx)
        return result