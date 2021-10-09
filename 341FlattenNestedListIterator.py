#sol1: flatten when init by recursive function
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nested_list):
            if not nested_list:
                return []
            result = []
            for data in nested_list:
                if data.isInteger():
                    result.append(data.getInteger())
                else:
                    result += flatten(data.getList())
            return result
        self.idx = 0
        self.array = flatten(nestedList)
        
    def next(self) -> int:
        ret = self.array[self.idx]
        self.idx += 1
        return ret
    
    def hasNext(self) -> bool:
        return self.idx != len(self.array)

#sol2: flatten when init by two stacks
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))
        self.array = []
        while True:
            if self.stack and not self.stack[-1].isInteger():
                pop_item = self.stack.pop().getList()
                self.stack += reversed(pop_item)
            elif self.stack:
                self.array.append(self.stack.pop().getInteger())
            else:
                break
        self.idx = 0
            

    def next(self) -> int:
        ret = self.array[self.idx]
        self.idx += 1
        return ret
    
    def hasNext(self) -> bool:
        return self.idx != len(self.array)
         
#sol3: one stack, append in stack by reversed order
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        while self.stack and not self.stack[-1].isInteger():
            pop_item = self.stack.pop().getList()
            self.stack += reversed(pop_item)
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            pop_item = self.stack.pop().getList()
            self.stack += reversed(pop_item)
        return len(self.stack) > 0