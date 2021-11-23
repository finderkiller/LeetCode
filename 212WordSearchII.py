#sol1: brute force, time: O(w*m*n*3^L), depth: O(L), extra: O(w*L)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return False
        self.width = len(board[0])
        self.height = len(board)
        result = []
        for word in words:
            find = False
            for row in range(self.height):
                for col in range(self.width):
                    if self.helper(board, row, col, word):
                        result.append(word)
                        find = True
                        break
                if find:
                    break
        return result
        
    def helper(self, board, row, col, word):
        if not word:
            return True
        if row < 0 or row == self.height:
            return False
        if col < 0 or col == self.width:
            return False
        if board[row][col] != word[0]:
            return False
        char = board[row][col]
        board[row][col] = "-"
        result = self.helper(board, row+1, col, word[1:]) or \
               self.helper(board, row-1, col, word[1:]) or \
               self.helper(board, row, col+1, word[1:]) or \
               self.helper(board, row, col-1, word[1:])
        board[row][col] = char
        return result

#sol2: Trie, time: O(m*n*3^L), depth: O(L), extra: O(w*L)
class Node:
    def __init__(self):
        self.children = [None]*26
        self.string = ""
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        ptr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not ptr.children[index]:
                ptr.children[index] = Node()
            ptr = ptr.children[index]
        ptr.string = word
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return False
        self.width = len(board[0])
        self.height = len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        self.result = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.helper(board, row, col, trie.root)
        return self.result
        
    def helper(self, board, row, col, parent_node):
        if row < 0 or row == self.height:
            return
        if col < 0 or col == self.width:
            return
        char = board[row][col]
        if char == "-":
            return
        index = ord(char) - ord('a')
        if not parent_node.children[index]:
            return
        if parent_node.children[index].string:
            self.result.append(parent_node.children[index].string)
            parent_node.children[index].string = ""
        board[row][col] = "-"
        self.helper(board, row+1, col, parent_node.children[index])
        self.helper(board, row-1, col, parent_node.children[index])
        self.helper(board, row, col+1, parent_node.children[index])
        self.helper(board, row, col-1, parent_node.children[index])
        board[row][col] = char

class Node:
    def __init__(self):
        self.children = [None]*26
        self.string = ""
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        ptr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not ptr.children[index]:
                ptr.children[index] = Node()
            ptr = ptr.children[index]
        ptr.string = word
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return False
        self.width = len(board[0])
        self.height = len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        self.result = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.helper(board, row, col, trie.root)
        return self.result
        
    def helper(self, board, row, col, parent_node):
        if row < 0 or row == self.height:
            return
        if col < 0 or col == self.width:
            return
        char = board[row][col]
        if char == "-":
            return
        index = ord(char) - ord('a')
        if not parent_node.children[index]:
            return
        if parent_node.children[index].string:
            self.result.append(parent_node.children[index].string)
            parent_node.children[index].string = ""
        board[row][col] = "-"
        self.helper(board, row+1, col, parent_node.children[index])
        self.helper(board, row-1, col, parent_node.children[index])
        self.helper(board, row, col+1, parent_node.children[index])
        self.helper(board, row, col-1, parent_node.children[index])
        board[row][col] = char