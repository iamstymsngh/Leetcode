from typing import List

"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    # TC -> O(nlogn)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_time = [interval.start for interval in intervals] # O(n)
        end_time = [interval.end for interval in intervals] # O(n)

        start_time.sort() # O(nlogn)
        end_time.sort() # O(nlogn)

        rooms_required, cur_rooms = 0, 0
        i, j = 0, 0
        while i < len(start_time):
            if start_time[i] < end_time[j]:
                cur_rooms += 1
                i+=1
            else:
                cur_rooms -= 1
                j += 1
            rooms_required = max(rooms_required, cur_rooms)
        return rooms_required

