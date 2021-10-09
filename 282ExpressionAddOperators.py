 def helper(self, start, num, collection, result, target):
        if start == len(num):
            string = ''.join(collection)[1:]
            if eval(string) == target:
                result.append(string)
            return
        for idx in range(start, len(num)):
            if idx != start and num[start] == '0':
                break
            collection.append("+" + num[start:idx+1])
            self.helper(idx+1, num, collection, result, target)
            collection.pop()
            if start == 0:
                continue
            collection.append("-" + num[start:idx+1])
            self.helper(idx+1, num, collection, result, target)
            collection.pop()
            collection.append("*" + num[start:idx+1])
            self.helper(idx+1, num, collection, result, target)
            collection.pop()