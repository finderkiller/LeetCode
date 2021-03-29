class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hash_table = {}

        for words in paragraph.split():
            if not words[-1].isalpha():
                words = words[:len(words)-1]
            for word in words.split(','):
                word = word.lower()
                if word not in hash_table:
                    hash_table[word] = 0
                hash_table[word] += 1        
        sorted_word_list = sorted(hash_table.keys(), key = lambda x:hash_table[x], reverse=True)     
        for word in sorted_word_list:
            if word in banned:
                continue
            return word