from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in numbers:
            # Check if num qualifies to be the start of the sequence
            if num - 1 not in numbers:
                # Yes, then check the longest consecutive sequence from this number
                length = 0
                while num + length in numbers:
                    length += 1
                longest = max(longest, length)
        return longest
