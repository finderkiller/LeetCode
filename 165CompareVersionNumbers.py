class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1:
            return -1
        if not version2:
            return 1
        v1 = version1.split(".")
        v2 = version2.split(".")
        len1 = len(v1)
        len2 = len(v2)
        diff = abs(len1-len2)
        if len1 > len2:
            while diff > 0:
                v2.append("0")
                diff -= 1
        elif len2 > len1:
            while diff > 0:
                v1.append("0")
                diff -= 1
        idx = 0
        while True:
            if idx == len(v1) and idx == len(v2):
                return 0
            if int(v1[idx]) < int(v2[idx]):
                return -1
            if int(v1[idx]) > int(v2[idx]):
                return 1
            idx +=1
        return 0