class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []
        result = []
        table = {}
        for string in strings:
            first_char_standard = ord(string[0])
            key_items = []
            for char in string:
                item = ord(char)-first_char_standard
                if item < 0:
                    item += 26
                key_items.append(item)
            key = tuple(key_items)
            if key not in table:
                table[key] = []
            table[key].append(string)
        
        for key, string_list in table.items():
            result.append(string_list)
        return result