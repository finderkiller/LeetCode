class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        i = -1
        j = 0
        count = 1
        while j < len(chars):
            if j+1 < len(chars) and chars[j] == chars[j+1]:
                count += 1
                j += 1
                continue
            i += 1
            chars[i] = chars[j]
            if count != 1:
                for digit in str(count):
                    i += 1 
                    chars[i] = digit
                count = 1
            j += 1                
        return min(len(chars), i+1)