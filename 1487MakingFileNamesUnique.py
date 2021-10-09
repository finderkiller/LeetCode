#brute force: time: O(n*k), k is the worst duplicated counts
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_set = set()
        result = []
        for name in names:
            if name not in name_set:
                name_set.add(name)
                result.append(name)
                continue
            k = 1
            while True:
                tmp_name = name + "(" + str(k) + ")"
                if tmp_name not in name_set:
                    name_set.add(tmp_name)
                    result.append(tmp_name)
                    break
                k += 1
        return result

#hash_table: time: O(n*k), k is the worst duplicated counts between last same name
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_table = {}
        result = []
        for name in names:
            if name not in name_table:
                name_table[name] = 0
                result.append(name)
                continue
            k = name_table.get(name) + 1
            tmp_name = name + "(" + str(k) + ")"
            while tmp_name in name_table:
                k += 1
                tmp_name = name + "(" + str(k) + ")"
            name_table[name] = k
            name_table[tmp_name] = 0
            result.append(tmp_name)
        return result