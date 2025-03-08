# Question -> https://neetcode.io/problems/meeting-schedule

"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List
class Solution:
    # TC - O(nlogn)
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        sorted_intervals = sorted(intervals, key = lambda x:x.start)

        # Do merge intervals logic
        merged_meetings = [sorted_intervals[0]]
        for i in range(len(sorted_intervals)):
            prev_interval = merged_meetings[-1]
            # Conflict
            if sorted_intervals[i].start < prev_interval.end:
                merged_meetings[-1].end = max(merged_meetings[-1].end, sorted_intervals[i].end)
            else:
                merged_meetings.append(sorted_intervals[i])


        # Check if possible to attend all meetings
        return True if len(merged_meetings) == len(intervals) else False