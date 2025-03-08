from typing import List

class Solution:
    # TC - O(nlogn)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        sorted_intervals = sorted(intervals, key = lambda x:x[0])

        # Do merge intervals logic
        merged = [sorted_intervals[0]]
        for i in range(len(sorted_intervals)):
            prev_interval = merged[-1]
            # Conflict
            if sorted_intervals[i][0] <= prev_interval[1]:
                merged[-1][1] = max(merged[-1][1], sorted_intervals[i][1])
            else:
                merged.append(sorted_intervals[i])
        return merged
