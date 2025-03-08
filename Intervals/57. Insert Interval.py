from typing import List

class Solution:
    # TC - O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output_intervals = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                output_intervals.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                output_intervals.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        output_intervals.append(newInterval)
        return output_intervals