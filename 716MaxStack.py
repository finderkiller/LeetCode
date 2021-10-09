# two stack, push:O(1), pop:O(1), top:O(1), peekMax: O(1), popMax:O(n)

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or self.max_stack[-1] <= x:
            self.max_stack.append(x)
    
    def pop(self) -> int:
        result = self.stack.pop()
        if result == self.max_stack[-1]:
            self.max_stack.pop()
        return result
    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_value = self.max_stack.pop()
        tmp_stack = []
        while len(self.stack) > 0 and self.stack[-1] != max_value:
            tmp_stack.append(self.stack.pop())
        self.stack.pop()
        while len(tmp_stack) > 0:
            self.push(tmp_stack.pop())
        return max_value

# stack+heap+hash_table, push:O(logn), pop:O(1), top:O(1), peekMax: O(1), popMax:O(1)