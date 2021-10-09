    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        input = path.split('/')
        output = []
        for value in input:
            if value == "." or value == "":
                continue
            if value == "..":
                if len(output) > 0:
                    output.pop()
                continue
            output.append(value)
        return '/'+'/'.join(output)