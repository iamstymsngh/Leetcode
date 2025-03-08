from typing import List

class Solution:
    # TC - O(nlogn)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda x:(x[0],x[1]))
        remove_count = 0
        prev_end = float("-inf")

        for start, end  in sorted_intervals:
            # No overlap
            if start >= prev_end:
                prev_end = end
            else:
                # Which interval to remove
                prev_end = min(prev_end, end)
                remove_count += 1
        return remove_count
