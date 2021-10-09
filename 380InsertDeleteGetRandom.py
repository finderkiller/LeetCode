#index_hash_table + list
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_table = {}
        self.array = []
        #record size of list, without calulate length of it which cost O(n)
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index_table:
            return False
        self.index_table[val] = self.size
        self.array.append(val)
        self.size += 1
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # swap last_value and val in array, O(1)
        if val not in self.index_table:
            return False
        index = self.index_table.get(val)
        last_val = self.array[self.size-1]
        self.array[index] = last_val
        self.index_table[last_val] = index
        self.index_table.pop(val)
        self.array.pop()
        self.size -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return self.array[random.randint(0, self.size-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()