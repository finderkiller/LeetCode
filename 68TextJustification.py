#time O(s), space: O(s)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_start = 0
        while line_start < len(words):
            line_end = line_start
            line_length = 0
            while line_end < len(words) and \
                  line_length + len(words[line_end]) + line_end-line_start <= maxWidth:
                line_length += len(words[line_end])
                line_end += 1
            string = ""
            space_total = maxWidth - line_length
            for i in range(line_start, line_end):
                string += words[i]
                space_count = 0
                if line_end == len(words):
                    if i < line_end-1:
                        space_count = 1
                    else:
                        space_count = space_total
                else:
                    if i < line_end-1:
                        if space_total%(line_end-1-i) == 0:
                            space_count = space_total//(line_end-1-i)
                        else:
                            space_count = space_total//(line_end-1-i)+1
                    else:
                        space_count = space_total
                string += "".join([" " for i in range(space_count)])
                space_total -= space_count
            result.append(string)
            line_start = line_end
        return result