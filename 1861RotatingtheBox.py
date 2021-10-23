class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not box:
            return
        m = len(box)
        n = len(box[0])
        result = [["." for i in range(m)] for i in range(n)]
        for i in range(m):
            k = n
            for j in range(n-1, -1, -1):
                if box[i][j] == ".":
                    continue
                if box[i][j] == "#":
                    k -= 1
                    result[k][m-1-i] = "#"
                elif box[i][j] == "*":
                    k = j
                    result[k][m-1-i] = "*"
        return result