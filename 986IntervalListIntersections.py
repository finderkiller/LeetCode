#O(n)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx_first = 0
        idx_second = 0
        result = []
        while idx_first < len(firstList) and idx_second < len(secondList):
            first_item = firstList[idx_first]
            second_item = secondList[idx_second]
            if (first_item[0] >= second_item[0] and first_item[0] <= second_item[1]) or \
               (second_item[0] >= first_item[0] and second_item[0] <= first_item[1]):
                left_bound = max(first_item[0], second_item[0])
                right_bound = min(first_item[1], second_item[1])
                result.append([left_bound, right_bound])
                if right_bound < second_item[1]:
                    secondList[idx_second] = [right_bound+1, second_item[1]]
                    idx_first += 1
                elif right_bound < first_item[1]:
                    firstList[idx_first] = [right_bound+1, first_item[1]]
                    idx_second += 1
                else:
                    idx_first += 1
                    idx_second += 1
            elif second_item[0] > first_item[1]:       
                idx_first += 1
            else:
                idx_second += 1
        return result

#O(n), less code
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx_first = 0
        idx_second = 0
        result = []
        while idx_first < len(firstList) and idx_second < len(secondList):
            first_item = firstList[idx_first]
            second_item = secondList[idx_second]
            left_bound = max(first_item[0], second_item[0])
            right_bound = min(first_item[1], second_item[1])
            if left_bound <= right_bound:
                result.append([left_bound, right_bound])
            if first_item[1] < second_item[1]:       
                idx_first += 1
            else:
                idx_second += 1
        return result