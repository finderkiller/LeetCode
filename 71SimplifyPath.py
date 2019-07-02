class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        input = path.split('/')
        result = []
        for value in input:
            value = value.strip("/")
            if value == "." or value == "":
                continue
            if value == "..":
                if len(result) > 0:
                    result.pop()
                continue
            result.append(value)
        return "/"+"/".join(result)
            
