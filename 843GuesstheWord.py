# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for i in range(10):
            guess_word = wordlist[random.randint(0, len(wordlist)-1)]
            count = master.guess(guess_word)
            if count == 6:
                return
            word_pool = []
            for word in wordlist:
                if word == guess_word:
                    continue
                if self.match(word, guess_word) == count:
                    word_pool.append(word)
            wordlist = word_pool
            
    def match(self, str_a, str_b):
        count = 0
        for idx in range(len(str_a)):
            if str_a[idx] == str_b[idx]:
                count += 1
        return count